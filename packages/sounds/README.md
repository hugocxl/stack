# @hugocxl/sounds

Tactile interface sounds for the web. Every sound is synthesized live with Web Audio from a
few layers of filtered noise and tone, so there are no audio files to load and nothing
plays the same way twice.

[Listen to the sounds](https://hugocxl.github.io/sounds/listen.html) · [Read the docs](https://hugocxl.github.io/sounds/docs.html)

```sh
npm install @hugocxl/sounds
```

```ts
import { play, haptic } from "@hugocxl/sounds";

button.addEventListener("pointerdown", () => play("down"));
button.addEventListener("pointerup", () => play("up"));

haptic("success"); // plays "success" and vibrates where the device supports it
```

## Sounds

| Group | Sounds |
| --- | --- |
| Press | `down`, `down-primary`, `up` |
| Latch | `latch-down`, `latch-up` |
| Selection | `tick`, `blip` |
| Typing | `type`, `type-space`, `type-big`, `type-up` |
| Overlay | `open` |
| Status | `success`, `warning`, `error` |

Haptics: `selection`, `light`, `medium`, `heavy`, `rigid`, `soft`, `success`, `warning` and `error`.

## API

- `play(sound)` plays a sound by name, or your own `{ layers }`.
- `haptic(kind)` plays the sound for an iOS-style haptic and vibrates.
- `setEnabled(on)`, `isEnabled()` and `setVolume(value)` control every sound.
- `render(context, destination, sound, time?, options?)` schedules a sound on any `BaseAudioContext`.
- `toWav(sound)` renders a sound into a WAV `Blob`.
- `sounds`, `soundNames`, `groups` and `feedback` describe the catalog.

Browsers only start audio after a user gesture, so call `play` from an event handler the
first time. The package is safe to import during server rendering. It does nothing until it
plays.

AI agents: the package ships a skill in `skills/sounds/` that maps every control to its
sound.

## License

MIT. See [NOTICE](NOTICE) for credits.
