// Locate a project and the @hugocxl libraries installed in it.
import { existsSync, readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

/** The four libraries, in the order agents should read them. */
export const LIBRARIES = [
  { id: 'design-system', package: '@hugocxl/design-system', need: 'Type, color, spacing, layout, pages and components' },
  { id: 'icons', package: '@hugocxl/icons', need: 'Icons that label actions and kinds' },
  { id: 'vectors', package: '@hugocxl/vectors', need: 'Illustrations that explain an idea or a state' },
  { id: 'sounds', package: '@hugocxl/sounds', need: 'Sound and haptic feedback for direct actions' },
];

/** This package's own root, where the `stack` skill and the templates live. */
export const STACK_ROOT = fileURLToPath(new URL('../', import.meta.url));

export const stackVersion = () => JSON.parse(readFileSync(join(STACK_ROOT, 'package.json'), 'utf8')).version;

/** The nearest directory at or above `cwd` that has a package.json, or `cwd` itself. */
export function findRoot(cwd = process.cwd()) {
  let dir = resolve(cwd);
  for (;;) {
    if (existsSync(join(dir, 'package.json'))) return dir;
    const parent = dirname(dir);
    if (parent === dir) return resolve(cwd);
    dir = parent;
  }
}

export function readManifest(root) {
  try {
    return JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));
  } catch {
    return {};
  }
}

/** The directory of an installed package as the project resolves it, or null. */
export function packageDir(root, name) {
  // Node caches resolutions per process, so confirm the file is still there.
  try {
    const manifest = createRequire(join(root, 'package.json')).resolve(`${name}/package.json`);
    return existsSync(manifest) ? dirname(manifest) : null;
  } catch {
    return null;
  }
}

/** Every library with its install state: `dir`, `version` and `skillDir` when installed. */
export function libraries(root) {
  return LIBRARIES.map(library => {
    const dir = packageDir(root, library.package);
    if (!dir) return { ...library, installed: false };
    const { version } = JSON.parse(readFileSync(join(dir, 'package.json'), 'utf8'));
    const skillDir = join(dir, 'skills', library.id);
    return { ...library, installed: true, dir, version, skillDir: existsSync(join(skillDir, 'SKILL.md')) ? skillDir : null };
  });
}

/** The project's `stack` settings from package.json. */
export function settings(root) {
  const config = readManifest(root).stack ?? {};
  return { rules: config.rules ?? {}, ignore: config.ignore ?? [] };
}
