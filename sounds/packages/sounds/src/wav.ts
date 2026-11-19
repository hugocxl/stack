import { render, duration } from "./engine.js";
import type { Sound, SoundName } from "./catalog.js";

/** Render a sound offline, without variation, into a 16-bit mono WAV. */
export async function toWav(sound: SoundName | Sound, sampleRate = 48000, gain = 0.55): Promise<Blob> {
  const ctx = new OfflineAudioContext(1, Math.ceil(duration(sound) * sampleRate), sampleRate);
  const out = ctx.createGain();
  out.gain.value = gain;
  out.connect(ctx.destination);
  render(ctx, out, sound, 0, { humanize: false });
  const samples = (await ctx.startRendering()).getChannelData(0);

  const view = new DataView(new ArrayBuffer(44 + samples.length * 2));
  const text = (offset: number, s: string) => [...s].forEach((ch, i) => view.setUint8(offset + i, ch.charCodeAt(0)));
  text(0, "RIFF");
  view.setUint32(4, 36 + samples.length * 2, true);
  text(8, "WAVE");
  text(12, "fmt ");
  view.setUint32(16, 16, true);
  view.setUint16(20, 1, true);
  view.setUint16(22, 1, true);
  view.setUint32(24, sampleRate, true);
  view.setUint32(28, sampleRate * 2, true);
  view.setUint16(32, 2, true);
  view.setUint16(34, 16, true);
  text(36, "data");
  view.setUint32(40, samples.length * 2, true);
  samples.forEach((s, i) => view.setInt16(44 + i * 2, Math.max(-1, Math.min(1, s)) * 0x7fff, true));
  return new Blob([view], { type: "audio/wav" });
}
