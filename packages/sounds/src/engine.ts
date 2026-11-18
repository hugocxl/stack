import { sounds, feedback, type Feedback, type Layer, type Sound, type SoundName } from "./catalog.js";

const resolve = (sound: SoundName | Sound): Sound => (typeof sound === "string" ? sounds[sound] : sound);

export type RenderOptions = {
  /** Small random variation on every play, so repeats never sound identical. */
  humanize?: boolean;
};

const noiseBuffers = new WeakMap<BaseAudioContext, AudioBuffer>();

function noiseBuffer(ctx: BaseAudioContext): AudioBuffer {
  let buffer = noiseBuffers.get(ctx);
  if (!buffer) {
    buffer = ctx.createBuffer(1, ctx.sampleRate / 2, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < data.length; i++) data[i] = Math.random() * 2 - 1;
    noiseBuffers.set(ctx, buffer);
  }
  return buffer;
}

function envelope(ctx: BaseAudioContext, start: number, level: number, attack: number, decay: number): GainNode {
  const gain = ctx.createGain();
  gain.gain.setValueAtTime(0, start);
  gain.gain.linearRampToValueAtTime(level, start + attack);
  gain.gain.exponentialRampToValueAtTime(1e-4, start + decay);
  return gain;
}

function scheduleLayer(ctx: BaseAudioContext, out: AudioNode, time: number, layer: Layer, humanize: boolean) {
  const vary = (amount: number) => (humanize ? 1 + (Math.random() * 2 - 1) * amount : 1);
  const start = time + (layer.at ?? 0);

  if (layer.kind === "noise") {
    const source = ctx.createBufferSource();
    source.buffer = noiseBuffer(ctx);
    source.playbackRate.value = vary(0.1);
    const filter = ctx.createBiquadFilter();
    filter.type = layer.filter ?? "bandpass";
    filter.frequency.value = layer.freq * vary(0.06);
    filter.Q.value = layer.q ?? 1;
    const gain = envelope(ctx, start, layer.level * vary(0.15), 8e-4, layer.decay);
    source.connect(filter).connect(gain).connect(out);
    source.start(start, humanize ? Math.random() * 0.4 : 0);
    source.stop(start + layer.decay + 0.02);
  } else {
    const osc = ctx.createOscillator();
    osc.type = layer.wave ?? "sine";
    const freq = layer.freq * vary(0.04);
    const to = ((layer.to ?? layer.freq) / layer.freq) * freq;
    osc.frequency.setValueAtTime(freq, start);
    osc.frequency.exponentialRampToValueAtTime(Math.max(20, to), start + layer.decay);
    const gain = envelope(ctx, start, layer.level * vary(0.12), layer.attack ?? 0.001, layer.decay);
    osc.connect(gain).connect(out);
    osc.start(start);
    osc.stop(start + layer.decay + 0.02);
  }
}

/** Schedule a sound, by name or your own layers, on any audio context, live or offline. */
export function render(ctx: BaseAudioContext, out: AudioNode, sound: SoundName | Sound, time = ctx.currentTime, options: RenderOptions = {}) {
  for (const layer of resolve(sound).layers) scheduleLayer(ctx, out, time, layer, options.humanize ?? true);
}

/** Length of a sound in seconds, tails included. */
export function duration(sound: SoundName | Sound): number {
  return Math.max(...resolve(sound).layers.map((l) => (l.at ?? 0) + l.decay + 0.02));
}

let ctx: AudioContext | null = null;
let master: GainNode | null = null;
let enabled = true;
let volume = 0.55;

function context(): AudioContext | null {
  if (ctx?.state === "closed") ctx = null;
  if (!ctx) {
    const Ctor = globalThis.AudioContext ?? (globalThis as any).webkitAudioContext;
    if (!Ctor) return null;
    ctx = new Ctor({ latencyHint: "interactive" }) as AudioContext;
    master = ctx.createGain();
    master.gain.value = volume;
    master.connect(ctx.destination);
  }
  if (ctx.state !== "running") ctx.resume().catch(() => {});
  return ctx;
}

/** Play a sound now. Call from a user gesture the first time, so the browser lets audio start. */
export function play(sound: SoundName | Sound) {
  if (!enabled) return;
  const c = context();
  if (c && master) render(c, master, sound, c.currentTime + 0.002);
}

/** Play the sound for a haptic, and vibrate where the device supports it. */
export function haptic(kind: Feedback) {
  play(feedback[kind].sound);
  if (typeof navigator !== "undefined" && typeof navigator.vibrate === "function") {
    navigator.vibrate(feedback[kind].vibrate);
  }
}

export function setEnabled(on: boolean) {
  enabled = on;
}

export function isEnabled() {
  return enabled;
}

/** Volume of every sound, from 0 to 1. The default is 0.55. */
export function setVolume(value: number) {
  volume = value;
  if (master) master.gain.value = value;
}
