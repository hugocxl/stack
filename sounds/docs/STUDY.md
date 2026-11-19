# Study: SPEC-01 interface sounds

Source: https://spec-01.vercel.app (bundle `assets/index-xquHoGQL.js`, fetched 2026-11-18).

SPEC-01 ships **no audio files**. Every sound is synthesized live with the Web Audio API
from two primitives, and the whole kit is about 40 lines of code.

## The two primitives

**Noise click.** Half a second of white noise, generated once, played from a random
offset at a random playback rate (±10%) through one biquad filter (bandpass by default).
The gain jumps to its peak in 0.8 ms and falls exponentially to silence. That fast
attack is what makes it read as a physical click instead of a hiss.

**Tone body.** An oscillator (sine by default) that glides exponentially from `freq` to
`to` over the decay. A short downward sweep, such as 210 → 130 Hz in 50 ms, gives the
"thock" of a key bottoming out.

## Why it feels tactile

- **Click plus body.** Most presses layer a bright 2–4 kHz noise click with a low
  100–300 Hz falling tone: the plastic and the mass.
- **Down and up are different sounds.** A press is lower and louder, and a release is
  higher, shorter and quieter (`down` vs `up`, `type` vs `type-up`).
- **Weight comes from pitch.** `down-primary` is the same recipe as `down`, about 20%
  lower and longer.
- **Springs ring.** `latch-*` and `type-space` add a delayed (3–6 ms), narrow
  (Q 6–14) noise band that rings like a spring or a stabilizer.
- **Nothing repeats exactly.** Every play varies filter frequency ±6%, pitch ±4% and
  level ±12–15%.
- **Tiny decays.** 6–70 ms for interaction sounds. Only the status chimes go past 100 ms.
- **Quiet master.** One shared gain of 0.55, and individual levels mostly under 0.4.
- **Musical status sounds.** success is E6 → A6 (a rising fourth), warning repeats A5 on a
  triangle wave, and error falls A3 → G3 on a square wave.

## How it is wired

- `pointerdown` on buttons plays `down` (or `down-primary` for `data-tone="primary"`),
  and the matching release plays `up`.
- Checkboxes play `latch-down` when checking and `up` when unchecking.
- Keys in text fields play `type`, `type-space` or `type-big`, `type-up` on release, and
  `tick` for auto-repeat.
- Popovers, menus and dialogs play `open`, through a MutationObserver on `data-open`
  that is throttled to 150 ms after any other sound.
- Sliders, wheels, tabs and segments play `selection`: `tick`, or `blip` when the focus
  is on an LCD or list.
- Haptics: `navigator.vibrate` where available, and the iOS `<input switch>` trick on Safari.
- Global throttle: 30 ms between haptics. Mute is stored in `localStorage["spec01:sound"]`.

## Not ported yet

- **MX-1 MIDI synth.** Triangle, square or saw voice through a resonant lowpass (Q 7)
  that sweeps from 2.2× the cutoff to the cutoff, level 0.16.
- **TM-1 timer chime.** Three 1320 Hz sine pips, 0.3 s apart, level 0.2, 0.22 s decay.

## Making them ours

The values above are SPEC-01's. `@hugocxl/sounds` keeps the method and changes the voice:

- Every tone sits on a note of G major (G2, D3, G3, B3, D4 and up), so sounds that overlap stay consonant.
- Clicks sit about 8% lower, with slightly longer decays, for a warmer and softer plastic.
- Springs ring higher and longer (Q 14–16).
- `blip` is a triangle instead of a square, softer on the ear.
- `open` rises a perfect fifth, from A4 to E5.
- success is a three-note G major arpeggio, warning repeats F#5, and error falls B3 to G3 on a triangle with a quiet square edge.
