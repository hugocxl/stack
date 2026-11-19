import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { main } from '../src/cli.mjs';
import { project, run } from './helpers.mjs';

test('help, version and unknown commands', async () => {
  assert.equal((await run(main, ['--help'])).code, 0);
  assert.match((await run(main, ['--help'])).output, /unknown-icon/);
  assert.equal((await run(main, [])).code, 2);
  assert.equal((await run(main, ['deploy'])).code, 2);
  assert.equal((await run(main, ['check', '--nope'])).code, 2);
  const { version } = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8'));
  assert.equal((await run(main, ['--version'])).output, version);
});

test('init sets up a project, then check passes', async () => {
  const root = project({ files: { 'src/a.tsx': "import { SearchIcon } from '@hugocxl/icons/react/stroke';\n" } });
  const init = await run(main, ['init', '--cwd', root]);
  assert.equal(init.code, 0);
  assert.match(init.output, /created {2}AGENTS\.md/);
  assert.match(init.output, /npx @hugocxl\/stack check/);
  assert.ok(existsSync(join(root, '.claude/skills/stack/SKILL.md')));
  const checked = await run(main, ['check', '--cwd', root]);
  assert.equal(checked.code, 0, checked.output);
  assert.match(checked.output, /Checked 1 file: 0 errors, 0 warnings\./);
  assert.match((await run(main, ['sync', '--cwd', join(root, 'src')])).output, /already up to date/);
});

test('init lists the libraries still to install', async () => {
  const root = project({ libraries: ['icons'] });
  const { output } = await run(main, ['init', '--cwd', root]);
  assert.match(output, /Not installed yet: npm install @hugocxl\/design-system @hugocxl\/vectors @hugocxl\/sounds/);
});

test('check exits 1 on errors, and on warnings with --strict', async () => {
  const root = project({ files: { 'src/a.tsx': '<div className="bg-blue-500" />' } });
  await run(main, ['sync', '--cwd', root]);
  assert.equal((await run(main, ['check', '--cwd', root])).code, 0);
  assert.equal((await run(main, ['check', '--cwd', root, '--strict'])).code, 1);
  const json = JSON.parse((await run(main, ['check', '--cwd', root, '--json'])).output);
  assert.deepEqual([json.errors, json.warnings, json.findings[0].rule], [0, 1, 'tailwind-palette']);
  const broken = project({ files: { 'src/a.tsx': '<svg data-icon="nope" />' } });
  await run(main, ['sync', '--cwd', broken]);
  const result = await run(main, ['check', '--cwd', broken]);
  assert.equal(result.code, 1);
  assert.match(result.output, /src\/a\.tsx:1:6 {2}error +There is no icon named "nope"/);
});

test('the bin runs', () => {
  const output = execFileSync('node', [new URL('../bin/stack.mjs', import.meta.url).pathname, '--version'], { encoding: 'utf8' });
  assert.match(output, /^\d+\.\d+\.\d+/);
});
