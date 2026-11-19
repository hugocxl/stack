import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";

test("the npm package ships the build, types, license and readme only", () => {
  const [pack] = JSON.parse(execFileSync("npm", ["pack", "-w", "@hugocxl/sounds", "--dry-run", "--json", "--ignore-scripts"], { encoding: "utf8" }));
  const files = pack.files.map((file) => file.path);
  for (const expected of ["dist/index.js", "dist/index.d.ts", "README.md", "package.json"]) {
    assert.ok(files.includes(expected), `ships ${expected}`);
  }
  assert.ok(!files.some((file) => file.startsWith("src/")), "does not ship sources");
});

test("the package resolves by name", async () => {
  const sounds = await import("@hugocxl/sounds");
  assert.equal(typeof sounds.play, "function");
  assert.equal(typeof sounds.toWav, "function");
});
