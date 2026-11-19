import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";
import * as library from "@hugocxl/sounds";

const skill = readFileSync("packages/sounds/skills/sounds/SKILL.md", "utf8");

test("the skill has valid frontmatter", () => {
  const [, front] = skill.match(/^---\n([\s\S]*?)\n---\n/) ?? [];
  assert.ok(front, "frontmatter");
  assert.match(front, /^name: sounds$/m);
  const description = front.match(/^description: (.+)$/m)?.[1] ?? "";
  assert.ok(description.length > 50 && description.length <= 1024, "description length");
});

test("the skill's table names every sound, and only real ones", () => {
  const table = skill.slice(skill.indexOf("## Choose the sound"), skill.indexOf("Haptics, if"));
  const named = new Set([...table.matchAll(/`([a-z-]+)`/g)].map((m) => m[1]).filter((name) => !["pointerdown", "pointerup", "keyup"].includes(name)));
  assert.deepEqual([...named].sort(), [...library.soundNames].sort());
});

test("the skill maps every haptic kind to its real sound", () => {
  const line = skill.slice(skill.indexOf("The kinds are"), skill.indexOf("## Use it"));
  for (const [kind, { sound }] of Object.entries(library.feedback)) {
    assert.match(line, new RegExp(`\`${kind}\``), kind);
    if (kind !== sound) assert.ok(line.includes(sound), `${kind} → ${sound}`);
  }
});

test("every function and sound the examples call exists", () => {
  for (const [, names] of skill.matchAll(/import \{ ([^}]+) \} from '@hugocxl\/sounds'/g)) {
    for (const name of names.split(",").map((s) => s.trim())) assert.ok(name in library, name);
  }
  for (const [, name] of skill.matchAll(/play\('([a-z-]+)'\)/g)) assert.ok(library.soundNames.includes(name), name);
  for (const [, name] of skill.matchAll(/haptic\('([a-z]+)'\)/g)) assert.ok(name in library.feedback, name);
});

test("the npm package ships the skill", () => {
  const [pack] = JSON.parse(execFileSync("npm", ["pack", "-w", "@hugocxl/sounds", "--dry-run", "--json", "--ignore-scripts"], { encoding: "utf8" }));
  assert.ok(pack.files.some((file) => file.path === "skills/sounds/SKILL.md"));
});
