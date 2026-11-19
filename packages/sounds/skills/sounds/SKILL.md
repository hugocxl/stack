---
name: sounds
description: Use @hugocxl/sounds to add tactile interface sounds and haptic feedback to a web interface — button presses, toggles, sliders, typing, menus and success, warning or error results. Covers which sound fits each control, wiring it to events, React, volume and mute, and custom sounds. Use it whenever you add audio or haptic feedback, or are tempted to add audio files or another sound library.
---

# @hugocxl/sounds

Fifteen short interface sounds, synthesized live with Web Audio from a few layers of filtered
noise and tone. There are no audio files to host, and nothing plays the same way twice.

## Rules

1. **Only these sounds.** Never add audio files, another UI sound library or a hand-rolled
   `AudioContext` for interface feedback.
2. **Sound confirms what the hand did.** Play a sound for a direct action: a press, a toggle,
   a step of a slider, a key, an overlay opening, the result of an action. Never for
   hover, scroll, page load, timers or anything the visitor did not do.
3. **Match the sound to the control.** Use the table below. The same control always makes the
   same sound across the product.
4. **Sound is optional.** It never carries information on its own: the interface shows every
   state too. Offer a setting to turn sounds off and respect it with `setEnabled`.
5. **Start from a gesture.** Browsers start audio only after the visitor interacts, so the
   first sound must come from `pointerdown`, `click` or `keydown`.

## Choose the sound

| Control or moment | Sound |
| --- | --- |
| A button going down and coming back up | `down` on `pointerdown`, `up` on `pointerup` |
| The page's main button | `down-primary`, then `up` |
| Checkbox, switch, toggle | `latch-down` when it turns on, `latch-up` when it turns off |
| Slider step, wheel, tab, segmented control | `tick` |
| Selection moving through a list or between screens | `blip` |
| A key in a text field | `type`; `type-space` for Space; `type-big` for Enter, Backspace, Delete and Tab; `type-up` on `keyup` |
| A menu, popover or dialog opening | `open` |
| The result of an action | `success`, `warning`, `error` |

Haptics, if you think in iOS terms: `haptic(kind)` plays the matching sound and vibrates where
the device supports it. The kinds are `selection` (tick), `light` (down), `medium` and
`heavy` (down-primary), `rigid` (latch-down), `soft` (latch-up), `success`, `warning` and
`error`.

## Use it

```sh
npm install @hugocxl/sounds
```

```ts
import { play, haptic } from '@hugocxl/sounds';

button.addEventListener('pointerdown', () => play('down'));
button.addEventListener('pointerup', () => play('up'));
form.addEventListener('submit', () => haptic('success'));
```

Sounds are plain function calls, so React needs no provider or hook:

```tsx
import { play } from '@hugocxl/sounds';

<button onPointerDown={() => play('down-primary')} onPointerUp={() => play('up')} onClick={save}>
  Save
</button>
```

Typing:

```ts
input.addEventListener('keydown', event => {
  if (event.repeat) return play('tick');
  if (event.key === ' ') play('type-space');
  else if (['Enter', 'Backspace', 'Delete', 'Tab'].includes(event.key)) play('type-big');
  else if (event.key.length === 1) play('type');
});
input.addEventListener('keyup', () => play('type-up'));
```

- Importing the package during server rendering is safe; nothing happens until a sound plays.
- `play` returns at once and never throws, so call it before the action's own work.
- Play the result sound (`success`, `warning`, `error`) when the result is known, not when the
  request starts.

## Volume and mute

```ts
import { setEnabled, setVolume, isEnabled } from '@hugocxl/sounds';

setVolume(0.4);    // 0 to 1, 0.55 by default
setEnabled(false); // mute every sound
```

Keep the visitor's choice in your own settings and call `setEnabled` when the page loads.

## Custom sounds and audio files

Add a new sound only when none of the fifteen fits. A sound is a list of layers: a `noise`
layer is a filtered burst of white noise (the click), a `tone` layer is an oscillator gliding
from `freq` to `to` (the body). Start from an existing one:

```ts
import { play, sounds } from '@hugocxl/sounds';

play({ layers: [...sounds.down.layers, { kind: 'tone', freq: 784, level: 0.1, decay: 0.08 }] });
```

`toWav(name)` renders a sound to a WAV `Blob` for native apps, videos or design tools.
`soundNames` lists every name and `feedback` maps each haptic kind to its sound.

## Check your work

- Every sound name is one of the fifteen in the table, and each control uses its row.
- No audio files or other sound libraries were added.
- Sounds play only for direct actions, and the product has a way to turn them off.

Full documentation: https://hugocxl.github.io/sounds/docs.html
