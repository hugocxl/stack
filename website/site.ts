// Site behavior: the pages play their own sounds, straight from the package source.
import { play, haptic, toWav, type Feedback, type SoundName } from "../packages/sounds/src/index.js";

// A button activated by keyboard sends a click with no pointer before it.
const pressed = (event: Event) => event.type === "pointerdown" || (event as MouseEvent).detail === 0;

for (const type of ["pointerdown", "click"]) {
  document.addEventListener(type, (event) => {
    if (type === "pointerdown" && (event as PointerEvent).button !== 0) return;
    if (!pressed(event)) return;
    const target = event.target as Element;
    const sound = target.closest<HTMLElement>("[data-sound]")?.dataset.sound;
    const kind = target.closest<HTMLElement>("[data-haptic]")?.dataset.haptic;
    if (sound) play(sound as SoundName);
    else if (kind) haptic(kind as Feedback);
    else if (target.closest(".ds-button")) play("down-primary");
    else if (target.closest(".ds-theme, .ds-code button, [data-wav]")) play("down");
  });
}

document.addEventListener("pointerup", (event) => {
  if ((event.target as Element).closest(".ds-button, .ds-theme, .ds-code button, [data-wav]")) play("up");
});

document.addEventListener("click", async (event) => {
  const name = (event.target as Element).closest<HTMLElement>("[data-wav]")?.dataset.wav;
  if (!name) return;
  const link = document.createElement("a");
  link.href = URL.createObjectURL(await toWav(name as SoundName));
  link.download = `${name}.wav`;
  link.click();
  URL.revokeObjectURL(link.href);
});

const typing = document.querySelector<HTMLInputElement>("#typing-field");
typing?.addEventListener("keydown", (event) => {
  if (event.metaKey || event.ctrlKey || event.altKey || event.isComposing) return;
  if (event.repeat) return play("tick");
  if (event.key === " ") play("type-space");
  else if (["Enter", "Backspace", "Delete", "Tab"].includes(event.key)) play("type-big");
  else if (event.key.length === 1) play("type");
});
typing?.addEventListener("keyup", (event) => {
  if (!event.metaKey && !event.ctrlKey && !event.altKey) play("type-up");
});
