import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { SYNONYMS, check, exportName, loadCatalog, search } from '../packages/icons/skills/icons/scripts/search.mjs';

const skill = readFileSync('packages/icons/skills/icons/SKILL.md', 'utf8');
const catalog = loadCatalog();
const names = new Set(catalog.map(icon => icon.name));

test('the skill has valid frontmatter', () => {
  const [, front] = skill.match(/^---\n([\s\S]*?)\n---\n/) ?? [];
  assert.ok(front, 'frontmatter');
  assert.match(front, /^name: icons$/m);
  const description = front.match(/^description: (.+)$/m)?.[1] ?? '';
  assert.ok(description.length > 50 && description.length <= 1024, 'description length');
});

test('every icon the skill names exists', () => {
  const referenced = [
    ...[...skill.matchAll(/data-icon="([a-z0-9-]+)"/g)].map(m => m[1]),
    ...[...skill.matchAll(/defaultColor\('([a-z0-9-]+)'/g)].map(m => m[1]),
    ...[...skill.matchAll(/`([a-z0-9-]+)` for (?:success|warning|error|info)/g)].map(m => m[1]),
    ...[...skill.matchAll(/--check ([a-z0-9 -]+?)\s{2,}/g)].flatMap(m => m[1].trim().split(/\s+/)),
  ];
  assert.ok(referenced.length >= 8);
  assert.deepEqual(referenced.filter(name => !names.has(name)), []);
});

test('every import in the skill resolves to a real export', () => {
  const imports = [...skill.matchAll(/import \{ ([^}]+) \} from '(@hugocxl\/icons[^']*)'/g)];
  assert.ok(imports.length >= 6);
  for (const [, specifiers, path] of imports) {
    const file = import.meta.resolve(path).replace(/\.js$/, '.d.ts');
    const types = readFileSync(new URL(file), 'utf8');
    for (const name of specifiers.split(',').map(s => s.trim())) {
      assert.match(types, new RegExp(`\\b${name}\\b`), `${path} exports ${name}`);
    }
  }
});

test('synonyms point at real icons', () => {
  for (const [word, targets] of Object.entries(SYNONYMS)) {
    for (const target of targets) assert.ok(names.has(target), `${word} → ${target}`);
  }
});

test('search ranks exact names and synonyms first', () => {
  assert.equal(search(catalog, 'trash')[0].name, 'trash');
  assert.equal(search(catalog, 'arrow right')[0].name, 'arrow-right');
  assert.ok(search(catalog, 'gear', { limit: 3 }).some(icon => icon.name === 'settings'));
  assert.ok(search(catalog, 'github', { style: 'stroke' }).every(icon => icon.styles.includes('stroke')));
  assert.equal(exportName('arrow-up-right'), 'ArrowUpRightIcon');
});

test('check reports unknown names with suggestions', () => {
  assert.deepEqual(check(catalog, ['search', 'trash']), []);
  const [missing] = check(catalog, ['serch']);
  assert.equal(missing.name, 'serch');
  assert.ok(missing.suggestions.includes('search'));
});

test('the command line exits non-zero for unknown names', () => {
  const script = 'packages/icons/skills/icons/scripts/search.mjs';
  assert.match(execFileSync('node', [script, '--check', 'search'], { encoding: 'utf8' }), /exist/);
  assert.throws(() => execFileSync('node', [script, '--check', 'not-an-icon'], { stdio: 'pipe' }));
});

test('the npm package ships the skill', () => {
  const [pack] = JSON.parse(execFileSync('npm', ['pack', '-w', '@hugocxl/icons', '--dry-run', '--json', '--ignore-scripts'], { encoding: 'utf8', maxBuffer: 256 * 1024 * 1024 }));
  const files = pack.files.map(file => file.path);
  assert.ok(files.includes('skills/icons/SKILL.md'));
  assert.ok(files.includes('skills/icons/scripts/search.mjs'));
});
