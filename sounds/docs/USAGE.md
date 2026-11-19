# Docs

Add tactile sounds to any web interface in a few lines. Every sound is synthesized in the browser, so there are no files to host.

## Install

```sh
npm install @hugocxl/sounds
```

The package has no dependencies and works with any bundler, in plain JavaScript, React, Vue, Svelte or anything else that runs in a browser.

## Play a sound

Call `play` with the name of a sound.

```ts
import { play } from "@hugocxl/sounds";

button.addEventListener("pointerdown", () => play("down"));
button.addEventListener("pointerup", () => play("up"));
```

Browsers only start audio after the visitor interacts with the page, so play the first sound from an event handler such as `pointerdown`, `click` or `keydown`. Importing the package during server rendering is safe: nothing happens until a sound plays.

## Choose the sound

| Group | Sound | Use it for |
| --- | --- | --- |
| Press | `down`, `up` | A button going down and coming back up |
| Press | `down-primary` | The main button, a little heavier |
| Latch | `latch-down`, `latch-up` | Checkboxes, switches and toggles |
| Selection | `tick` | Sliders, wheels, tabs and segmented controls |
| Selection | `blip` | A selection moving through a list or a screen |
| Typing | `type`, `type-space`, `type-big`, `type-up` | Keys in a text field. `type-big` is for Enter, Backspace, Delete and Tab |
| Overlay | `open` | A menu, popover or dialog opening |
| Status | `success`, `warning`, `error` | The result of an action |

## Haptics

If you already think in iOS haptics, call `haptic` instead. It plays the matching sound and vibrates on devices that support it.

```ts
import { haptic } from "@hugocxl/sounds";

haptic("selection"); // tick
haptic("medium");    // down-primary
haptic("success");   // success
```

The kinds are `selection`, `light`, `medium`, `heavy`, `rigid`, `soft`, `success`, `warning` and `error`.

## Typing

Give a text field the sound of a keyboard.

```ts
import { play } from "@hugocxl/sounds";

input.addEventListener("keydown", (event) => {
  if (event.repeat) return play("tick");
  if (event.key === " ") play("type-space");
  else if (["Enter", "Backspace", "Delete", "Tab"].includes(event.key)) play("type-big");
  else if (event.key.length === 1) play("type");
});
input.addEventListener("keyup", () => play("type-up"));
```

## In React

Sounds are plain function calls, so they need no provider or hook.

```tsx
import { play } from "@hugocxl/sounds";

export function SaveButton({ onSave }) {
  return (
    <button onPointerDown={() => play("down-primary")} onPointerUp={() => play("up")} onClick={onSave}>
      Save
    </button>
  );
}
```

## Volume and mute

```ts
import { setEnabled, setVolume } from "@hugocxl/sounds";

setVolume(0.4);    // from 0 to 1, 0.55 by default
setEnabled(false); // mute every sound, for example from a setting
```

Respect visitors who turn sound off: keep the choice in your own settings and call `setEnabled` when the page loads.

## Make your own

Every sound is a list of layers. A `noise` layer is a burst of white noise through a filter, the click. A `tone` layer is an oscillator gliding from `freq` to `to`, the body. Pass your own to `play`.

```ts
import { play, sounds } from "@hugocxl/sounds";

play({
  layers: [
    { kind: "noise", freq: 3000, q: 1, level: 0.3, decay: 0.02 },
    { kind: "tone", freq: 240, to: 150, level: 0.4, decay: 0.05 },
  ],
});

console.log(sounds.down.layers); // start from an existing sound
```

| Field | Layer | Meaning |
| --- | --- | --- |
| `at` | both | Delay from the start of the sound, in seconds |
| `freq` | both | Filter frequency for noise, start pitch for a tone, in hertz |
| `to` | tone | End pitch, reached at the end of the decay |
| `filter` | noise | A biquad filter type, `bandpass` by default |
| `q` | noise | How narrow the filter is. High values ring like a spring |
| `wave` | tone | `sine` by default, or `square`, `triangle` or `sawtooth` |
| `level` | both | Peak loudness, usually below 0.5 |
| `attack` | tone | Seconds to reach the peak, 0.001 by default |
| `decay` | both | Seconds to fall to silence |

## Export audio files

`toWav` renders any sound, without the play-to-play variation, into a WAV file. Use it for native apps, videos or design tools.

```ts
import { toWav } from "@hugocxl/sounds";

const blob = await toWav("success");
```

The [Listen](listen.html) page downloads every sound this way.

## Credits and license

The code and the sounds are MIT licensed. The catalog grew out of a study of the interface sounds of [SPEC-01](https://spec-01.vercel.app), and the [study notes](https://github.com/hugocxl/sounds/blob/main/docs/STUDY.md) describe what was learned from it.
