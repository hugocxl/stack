// The stack skill, the marketplace and the package, checked against the published libraries.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { check } from '../src/check.mjs';
import { LIBRARIES, packageDir } from '../src/project.mjs';

const root = new URL('../', import.meta.url).pathname;
const skill = readFileSync(join(root, 'skills/stack/SKILL.md'), 'utf8');
const json = path => JSON.parse(readFileSync(path, 'utf8'));
const icons = new Set(json(join(packageDir(root, '@hugocxl/icons'), 'dist/catalog.json')).map(icon => icon.name));
const vectors = new Set(json(join(packageDir(root, '@hugocxl/vectors'), 'dist/catalog.json')).map(vector => vector.name));
const sounds = await import('@hugocxl/sounds');

test('the stack skill has valid frontmatter', () => {
  const front = skill.match(/^---\n([\s\S]*?)\n---\n/)?.[1] ?? '';
  assert.match(front, /^name: stack$/m);
  const description = front.match(/^description: (.+)$/m)?.[1] ?? '';
  assert.ok(description.length > 50 && description.length <= 1024);
});

test('the stack skill names only real icons, vectors and sounds', () => {
  const quoted = [...skill.matchAll(/`([a-z]+(?:-[a-z]+)*)`/g)].map(m => m[1]);
  const iconNames = ['search', 'trash', 'folder', 'terminal'];
  const vectorNames = ['empty-inbox', 'payment-failed'];
  for (const name of iconNames) assert.ok(quoted.includes(name) && icons.has(name), name);
  for (const name of vectorNames) assert.ok(quoted.includes(name) && vectors.has(name), name);
  const table = skill.slice(skill.indexOf('| Design-system element'), skill.indexOf('Links that navigate'));
  const used = [...table.matchAll(/`([a-z-]+)`/g)].map(m => m[1]).filter(name => name !== 'button' && name !== 'form');
  assert.ok(used.length >= 8);
  for (const name of used) assert.ok(sounds.soundNames.includes(name), name);
});

test('the stack skill names every library and their skills', () => {
  for (const library of LIBRARIES) {
    assert.ok(skill.includes(`\`${library.package}\``), library.package);
    assert.ok(skill.includes(`| \`${library.id}\` |`), library.id);
  }
});

test('the export paths the stack skill uses exist', () => {
  for (const [, pkg, path] of skill.matchAll(/(@hugocxl\/(?:icons|vectors|design-system))\/([a-z.\-/]+?)(?:\/<name>)?[`";]/g)) {
    const manifest = json(join(packageDir(root, pkg), 'package.json'));
    const keys = Object.keys(manifest.exports);
    const sub = `./${path}`;
    assert.ok(keys.includes(sub) || keys.some(key => key.endsWith('/*') && sub.startsWith(key.slice(0, -1))), `${pkg}/${path}`);
  }
});

test('the marketplace lists the stack and one plugin per library', () => {
  const marketplace = json(join(root, '../.claude-plugin/marketplace.json'));
  assert.equal(marketplace.name, 'hugocxl');
  const [stack, ...rest] = marketplace.plugins;
  assert.deepEqual([stack.name, stack.source], ['stack', './ai']);
  assert.deepEqual(stack.dependencies, LIBRARIES.map(library => library.id));
  assert.deepEqual(rest.map(plugin => [plugin.name, plugin.source]), LIBRARIES.map(library => [library.id, { source: 'npm', package: library.package }]));
});

test('the published libraries pass their own checks in an empty project', async () => {
  const { findings } = await check(root, { files: [] });
  assert.deepEqual(findings.filter(finding => finding.rule !== 'agent-files'), []);
});

test('the npm package ships the CLI, the skill and the template only', () => {
  const [pack] = JSON.parse(execFileSync('npm', ['pack', '--dry-run', '--json', '--ignore-scripts'], { cwd: root, encoding: 'utf8' }));
  const files = pack.files.map(file => file.path).sort();
  assert.deepEqual(files, ['LICENSE', 'README.md', 'bin/ai.mjs', 'package.json', 'skills/stack/SKILL.md', 'src/check.mjs', 'src/cli.mjs', 'src/project.mjs', 'src/sync.mjs', 'templates/AGENTS.md']);
});
