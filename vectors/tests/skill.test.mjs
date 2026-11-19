import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { categories, check, loadCatalog, search } from '../packages/vectors/skills/vectors/scripts/search.mjs';

const skill = readFileSync('packages/vectors/skills/vectors/SKILL.md', 'utf8');
const catalog = loadCatalog();
const names = new Set(catalog.map(vector => vector.name));

test('the skill has valid frontmatter', () => {
  const [, front] = skill.match(/^---\n([\s\S]*?)\n---\n/) ?? [];
  assert.ok(front, 'frontmatter');
  assert.match(front, /^name: vectors$/m);
  const description = front.match(/^description: (.+)$/m)?.[1] ?? '';
  assert.ok(description.length > 50 && description.length <= 1024, 'description length');
});

test('every vector the skill names exists', () => {
  const referenced = [
    ...[...skill.matchAll(/@hugocxl\/vectors\/(?:react|react-native|js)\/([a-z0-9-]+)/g)].map(m => m[1]),
    ...[...skill.matchAll(/--check ([a-z0-9 -]+?)\s{2,}/g)].flatMap(m => m[1].trim().split(/\s+/)),
    ...[...skill.matchAll(/`([a-z0-9]+(?:-[a-z0-9]+)+)`/g)].map(m => m[1]).filter(name => !['react-native-svg', 'figure-wide', 'figure-grid', 'design-system', 'aria-hidden', 'aria-label'].includes(name)),
  ];
  assert.ok(referenced.length >= 6);
  assert.deepEqual(referenced.filter(name => !names.has(name)), []);
});

test('every import in the skill resolves to a real export', () => {
  const imports = [...skill.matchAll(/import \{ ([^}]+) \} from '(@hugocxl\/vectors[^']*)'/g)];
  assert.ok(imports.length >= 4);
  for (const [, specifiers, path] of imports) {
    const types = readFileSync(new URL(import.meta.resolve(path).replace(/\.js$/, '.d.ts')), 'utf8');
    for (const name of specifiers.split(',').map(s => s.trim())) assert.match(types, new RegExp(`\\b${name}\\b`), `${path} exports ${name}`);
  }
});

test('the skill names a real category in its example', () => {
  const ids = new Set(categories(catalog).map(c => c.id));
  for (const [, id] of skill.matchAll(/--category ([a-z-]+)/g)) assert.ok(ids.has(id), id);
});

test('search finds vectors by meaning', () => {
  assert.equal(search(catalog, 'empty inbox')[0].name, 'empty-inbox');
  assert.equal(search(catalog, 'no search results')[0].name, 'no-search-results');
  assert.equal(search(catalog, 'payment failed')[0].name, 'payment-failed');
  assert.ok(search(catalog, 'launch', { category: 'landing-and-marketing' }).every(v => v.categoryId === 'landing-and-marketing'));
});

test('check reports unknown names with suggestions', () => {
  assert.deepEqual(check(catalog, ['modular-design']), []);
  const [missing] = check(catalog, ['modlar-design']);
  assert.ok(missing.suggestions.includes('modular-design'));
  const script = 'packages/vectors/skills/vectors/scripts/search.mjs';
  assert.throws(() => execFileSync('node', [script, '--check', 'not-a-vector'], { stdio: 'pipe' }));
});

test('the npm package ships the skill', () => {
  const [pack] = JSON.parse(execFileSync('npm', ['pack', '-w', '@hugocxl/vectors', '--dry-run', '--json', '--ignore-scripts'], { encoding: 'utf8', maxBuffer: 256 * 1024 * 1024 }));
  const files = pack.files.map(file => file.path);
  assert.ok(files.includes('skills/vectors/SKILL.md'));
  assert.ok(files.includes('skills/vectors/scripts/search.mjs'));
});
