#!/usr/bin/env node
// Copy the design system's system/ folder verbatim into website/system/.
// The copy is committed so CI and Pages builds need no sibling checkout.
// Usage: node scripts/sync-design-system.mjs [path/to/design-system] [--check]
import { cpSync, existsSync, readFileSync, readdirSync, rmSync, statSync } from 'node:fs';
import { join, relative, resolve } from 'node:path';

const args = process.argv.slice(2);
const check = args.includes('--check');
const source = resolve(args.find(arg => !arg.startsWith('--')) ?? '../design-system', 'system');
const target = resolve('website/system');
if (!existsSync(source)) throw new Error(`Design system not found at ${source}`);

const files = root => readdirSync(root, { recursive: true })
  .filter(path => statSync(join(root, path)).isFile())
  .map(path => path.split('\\').join('/'))
  .sort();

if (check) {
  const expected = files(source);
  const actual = existsSync(target) ? files(target) : [];
  const differ = [...new Set([...expected, ...actual])].filter(path =>
    !expected.includes(path) || !actual.includes(path) ||
    !readFileSync(join(source, path)).equals(readFileSync(join(target, path))));
  if (differ.length) throw new Error(`website/system differs from ${source}: ${differ.join(', ')}`);
  console.log(`website/system matches ${relative(process.cwd(), source)} (${expected.length} files).`);
} else {
  rmSync(target, { recursive: true, force: true });
  cpSync(source, target, { recursive: true });
  console.log(`Copied ${files(target).length} files from ${relative(process.cwd(), source)} to website/system.`);
}
