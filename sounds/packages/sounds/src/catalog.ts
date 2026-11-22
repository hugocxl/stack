// Every sound is a short stack of layers, scheduled from the moment it plays.
//
// A noise layer is a burst of white noise through one biquad filter: the
// "click" of a key or a switch. A tone layer is an oscillator gliding from
// `freq` to `to`: the body of a press, or a chime. Both rise in `attack`
// seconds and fall exponentially to silence over `decay` seconds.
//
// Tones sit on notes of G major, so sounds played together never clash. The
// kit grew out of a study of the SPEC-01 interface sounds: see docs/STUDY.md.

export type NoiseLayer = {
  kind: "noise";
  /** Delay from the start of the sound, in seconds. */
  at?: number;
  filter?: BiquadFilterType;
  /** Filter frequency in hertz. */
  freq: number;
  q?: number;
  level: number;
  decay: number;
};

export type ToneLayer = {
  kind: "tone";
  at?: number;
  wave?: OscillatorType;
  /** Start frequency in hertz. */
  freq: number;
  /** End frequency in hertz, reached at the end of the decay. */
  to?: number;
  level: number;
  decay: number;
  attack?: number;
};

export type Layer = NoiseLayer | ToneLayer;

export type SoundName =
  | "down"
  | "down-primary"
  | "up"
  | "latch-down"
  | "latch-up"
  | "tick"
  | "detent"
  | "detent-fast"
  | "blip"
  | "type"
  | "type-space"
  | "type-big"
  | "type-up"
  | "open"
  | "success"
  | "warning"
  | "error";

export type SoundGroup = "press" | "latch" | "selection" | "typing" | "overlay" | "status";

export type Sound = {
  group?: SoundGroup;
  description?: string;
  layers: Layer[];
};

export const sounds: Record<SoundName, Sound> = {
  down: {
    group: "press",
    description: "A button pressed down.",
    layers: [
      { kind: "noise", freq: 2400, q: 0.9, level: 0.3, decay: 0.024 },
      { kind: "tone", freq: 196, to: 131, level: 0.4, decay: 0.055 },
    ],
  },
  "down-primary": {
    group: "press",
    description: "The main button pressed down: lower and heavier.",
    layers: [
      { kind: "noise", freq: 1900, q: 0.8, level: 0.34, decay: 0.028 },
      { kind: "tone", freq: 147, to: 98, level: 0.55, decay: 0.075 },
    ],
  },
  up: {
    group: "press",
    description: "A button released.",
    layers: [
      { kind: "noise", freq: 3600, q: 1.2, level: 0.15, decay: 0.013 },
      { kind: "tone", freq: 294, to: 262, level: 0.1, decay: 0.02 },
    ],
  },
  "latch-down": {
    group: "latch",
    description: "A checkbox or toggle latching on, with a ringing spring.",
    layers: [
      { kind: "noise", freq: 1800, q: 0.8, level: 0.18, decay: 0.02 },
      { kind: "tone", freq: 147, to: 110, level: 0.2, decay: 0.05 },
      { kind: "noise", at: 0.005, freq: 1320, q: 16, level: 0.035, decay: 0.055 },
    ],
  },
  "latch-up": {
    group: "latch",
    description: "A checkbox or toggle releasing.",
    layers: [
      { kind: "noise", freq: 3000, q: 1, level: 0.11, decay: 0.013 },
      { kind: "noise", at: 0.003, freq: 1760, q: 14, level: 0.03, decay: 0.045 },
    ],
  },
  tick: {
    group: "selection",
    description: "A detent: sliders, wheels, segmented controls.",
    layers: [
      { kind: "noise", filter: "highpass", freq: 3000, q: 0.7, level: 0.18, decay: 0.007 },
      { kind: "tone", freq: 3520, level: 0.03, decay: 0.012 },
    ],
  },
  detent: {
    group: "selection",
    description: "A wheel settling on a detent at a slow turn: a defined click with a short G6 ring.",
    layers: [
      { kind: "noise", freq: 2600, q: 2.4, level: 0.16, decay: 0.01 },
      { kind: "tone", freq: 1568, level: 0.05, decay: 0.02 },
    ],
  },
  "detent-fast": {
    group: "selection",
    description: "A detent passing at a fast spin: brighter and drier, with no ring.",
    layers: [
      { kind: "noise", filter: "highpass", freq: 4200, q: 0.7, level: 0.14, decay: 0.005 },
      { kind: "tone", freq: 3951, level: 0.02, decay: 0.006 },
    ],
  },
  blip: {
    group: "selection",
    description: "A selection moving on a screen or list: a soft triangle A6.",
    layers: [{ kind: "tone", wave: "triangle", freq: 1760, level: 0.06, decay: 0.05, attack: 0.002 }],
  },
  type: {
    group: "typing",
    description: "A key pressed in a text field.",
    layers: [
      { kind: "noise", freq: 3100, q: 1.1, level: 0.22, decay: 0.015 },
      { kind: "tone", freq: 247, to: 185, level: 0.18, decay: 0.032 },
    ],
  },
  "type-space": {
    group: "typing",
    description: "The space bar, with a little stabilizer rattle.",
    layers: [
      { kind: "noise", freq: 2000, q: 0.8, level: 0.26, decay: 0.024 },
      { kind: "tone", freq: 165, to: 117, level: 0.26, decay: 0.055 },
      { kind: "noise", at: 0.007, freq: 820, q: 7, level: 0.05, decay: 0.035 },
    ],
  },
  "type-big": {
    group: "typing",
    description: "Enter, Backspace, Delete and Tab.",
    layers: [
      { kind: "noise", freq: 2400, q: 0.9, level: 0.26, decay: 0.02 },
      { kind: "tone", freq: 196, to: 139, level: 0.28, decay: 0.05 },
    ],
  },
  "type-up": {
    group: "typing",
    description: "A key released.",
    layers: [{ kind: "noise", freq: 4200, q: 1.3, level: 0.08, decay: 0.009 }],
  },
  open: {
    group: "overlay",
    description: "A menu, popover or dialog opening: a click and a chirp rising a fifth.",
    layers: [
      { kind: "noise", freq: 2400, q: 1, level: 0.1, decay: 0.013 },
      { kind: "tone", freq: 440, to: 660, level: 0.045, decay: 0.07, attack: 0.004 },
    ],
  },
  success: {
    group: "status",
    description: "A rising G major arpeggio: D6, G6, B6.",
    layers: [
      { kind: "tone", freq: 1175, level: 0.06, decay: 0.08, attack: 0.004 },
      { kind: "tone", at: 0.06, freq: 1568, level: 0.06, decay: 0.09, attack: 0.004 },
      { kind: "tone", at: 0.12, freq: 1976, level: 0.06, decay: 0.18, attack: 0.004 },
    ],
  },
  warning: {
    group: "status",
    description: "Two even triangle beeps on F#5.",
    layers: [
      { kind: "tone", wave: "triangle", freq: 740, level: 0.09, decay: 0.09 },
      { kind: "tone", wave: "triangle", at: 0.12, freq: 740, level: 0.09, decay: 0.09 },
    ],
  },
  error: {
    group: "status",
    description: "Two falling triangle notes, B3 then G3, with a low square edge.",
    layers: [
      { kind: "tone", wave: "triangle", freq: 247, level: 0.12, decay: 0.1 },
      { kind: "tone", wave: "square", freq: 247, level: 0.02, decay: 0.08 },
      { kind: "tone", wave: "triangle", at: 0.13, freq: 196, level: 0.12, decay: 0.16 },
      { kind: "tone", wave: "square", at: 0.13, freq: 196, level: 0.02, decay: 0.12 },
    ],
  },
};

export const soundNames = Object.keys(sounds) as SoundName[];

export const groups: Record<SoundGroup, string> = {
  press: "Press",
  latch: "Latch",
  selection: "Selection",
  typing: "Typing",
  overlay: "Overlay",
  status: "Status",
};

/** iOS-style haptic feedback, each mapped to the sound it makes. */
export type Feedback =
  | "selection"
  | "light"
  | "medium"
  | "heavy"
  | "rigid"
  | "soft"
  | "success"
  | "warning"
  | "error";

export const feedback: Record<Feedback, { sound: SoundName; vibrate: number | number[] }> = {
  selection: { sound: "tick", vibrate: 8 },
  light: { sound: "down", vibrate: 12 },
  medium: { sound: "down-primary", vibrate: 22 },
  heavy: { sound: "down-primary", vibrate: 36 },
  rigid: { sound: "latch-down", vibrate: 14 },
  soft: { sound: "latch-up", vibrate: 18 },
  success: { sound: "success", vibrate: [14, 70, 22] },
  warning: { sound: "warning", vibrate: [24, 90, 24] },
  error: { sound: "error", vibrate: [28, 60, 28, 60, 28] },
};
