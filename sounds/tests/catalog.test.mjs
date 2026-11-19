import { test } from "node:test";
import assert from "node:assert/strict";
import { sounds, soundNames, groups, feedback, duration } from "../packages/sounds/dist/index.js";

test("every sound has a group, a description and valid layers", () => {
  for (const name of soundNames) {
    const sound = sounds[name];
    assert.ok(sound.group in groups, `${name} has a known group`);
    assert.ok(sound.description, `${name} has a description`);
    assert.ok(sound.layers.length > 0, `${name} has layers`);
    for (const layer of sound.layers) {
      assert.ok(["noise", "tone"].includes(layer.kind), `${name} layer kind`);
      assert.ok(layer.freq >= 20 && layer.freq <= 20000, `${name} frequency is audible`);
      assert.ok(layer.level > 0 && layer.level <= 1, `${name} level is between 0 and 1`);
      assert.ok(layer.decay > 0, `${name} decays`);
    }
  }
});

test("sounds stay short", () => {
  for (const name of soundNames) assert.ok(duration(name) < 0.5, `${name} is under half a second`);
});

test("every haptic maps to a sound", () => {
  for (const [kind, { sound }] of Object.entries(feedback)) assert.ok(sound in sounds, `${kind} plays ${sound}`);
});

test("importing without Web Audio is safe", async () => {
  const { play, haptic } = await import("../packages/sounds/dist/index.js");
  assert.doesNotThrow(() => play("down"));
  assert.doesNotThrow(() => haptic("success"));
});
