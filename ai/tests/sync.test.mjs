import { test } from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { BEGIN, END, plan, sync } from '../src/sync.mjs';
import { project } from './helpers.mjs';

const read = (root, path) => readFileSync(join(root, path), 'utf8');

test('sync writes AGENTS.md and every skill for every agent without CLAUDE.md', () => {
  const root = project();
  const { write } = sync(root);
  assert.ok(write.every(file => file.created));
  for (const base of ['.agents/skills', '.claude/skills']) {
    for (const id of ['stack', 'design-system', 'icons', 'vectors', 'sounds']) assert.ok(existsSync(join(root, base, id, 'SKILL.md')), `${base}/${id}`);
    assert.ok(existsSync(join(root, base, 'icons/scripts/search.mjs')));
  }
  assert.ok(!existsSync(join(root, 'CLAUDE.md')));
  const agents = read(root, 'AGENTS.md');
  assert.ok(agents.includes(BEGIN) && agents.includes(END));
  assert.match(agents, /`@hugocxl\/icons` \| `\.agents\/skills\/icons`/);
  assert.doesNotMatch(agents, /\{\{/);
  assert.equal(read(root, '.agents/skills/stack/SKILL.md'), readFileSync(new URL('../skills/stack/SKILL.md', import.meta.url), 'utf8'));
});

test('sync is idempotent', () => {
  const root = project();
  sync(root);
  const again = plan(root);
  assert.deepEqual([again.write, again.remove], [[], []]);
});

test('sync keeps what people wrote in AGENTS.md', () => {
  const root = project({ files: { 'AGENTS.md': '# My app\n\nUse pnpm.\n' } });
  sync(root);
  const agents = read(root, 'AGENTS.md');
  assert.ok(agents.startsWith('# My app\n\nUse pnpm.\n\n' + BEGIN));
  assert.ok(!existsSync(join(root, 'CLAUDE.md')));

  writeFileSync(join(root, 'AGENTS.md'), agents.replace('Use pnpm.', 'Use pnpm.\n\nRun the tests.') + '\n## Deploy\n\nFriday never.\n');
  sync(root);
  const updated = read(root, 'AGENTS.md');
  assert.match(updated, /Run the tests\./);
  assert.match(updated, /## Deploy\n\nFriday never\./);
  assert.equal(updated.split(BEGIN.slice(0, 26)).length, 2, 'one managed section');
});

test('sync follows upgrades and removals of libraries', () => {
  const root = project();
  sync(root);
  writeFileSync(join(root, 'node_modules/@hugocxl/icons/skills/icons/SKILL.md'), '---\nname: icons\ndescription: New.\n---\n');
  rmSync(join(root, 'node_modules/@hugocxl/icons/skills/icons/scripts'), { recursive: true });
  rmSync(join(root, 'node_modules/@hugocxl/sounds'), { recursive: true });
  const pending = plan(root);
  assert.ok(pending.write.some(file => file.path === '.claude/skills/icons/SKILL.md'));
  assert.ok(pending.remove.some(file => file.path === '.agents/skills/sounds/SKILL.md'));
  sync(root);
  assert.match(read(root, '.claude/skills/icons/SKILL.md'), /New\./);
  assert.ok(!existsSync(join(root, '.agents/skills/icons/scripts')));
  assert.ok(!existsSync(join(root, '.agents/skills/sounds')));
  assert.match(read(root, 'AGENTS.md'), /not installed: `npm install @hugocxl\/sounds`/);
});

test('a library without a skill asks for an upgrade', () => {
  const root = project();
  rmSync(join(root, 'node_modules/@hugocxl/vectors/skills'), { recursive: true });
  sync(root);
  assert.match(read(root, 'AGENTS.md'), /`@hugocxl\/vectors` \| upgrade the package to get its skill/);
  assert.ok(!existsSync(join(root, '.agents/skills/vectors')));
});

test('sync leaves other skills alone', () => {
  const root = project({ files: { '.claude/skills/deploy/SKILL.md': 'mine' } });
  sync(root);
  assert.equal(read(root, '.claude/skills/deploy/SKILL.md'), 'mine');
});
