import { test } from 'node:test';
import assert from 'node:assert/strict';
import { check, globToRegExp, importsOf } from '../src/check.mjs';
import { sync } from '../src/sync.mjs';
import { project } from './helpers.mjs';

async function findings(files, options = {}) {
  const root = project({ files, ...options });
  sync(root);
  return (await check(root)).findings;
}
const rules = list => list.map(finding => finding.rule);

test('a project that follows the stack passes', async () => {
  const result = await findings({
    'src/App.tsx': [
      "import { SearchIcon, TrashIcon } from '@hugocxl/icons/react/stroke';",
      "import { FolderIcon } from '@hugocxl/icons/react/stroke/folder';",
      "import { GithubIcon } from '@hugocxl/icons/react/github';",
      "import { defaultColor } from '@hugocxl/icons/colors';",
      "import { EmptyInboxVector } from '@hugocxl/vectors/react/empty-inbox';",
      "import { PaymentFailedVector } from '@hugocxl/vectors/react';",
      "import { play, haptic } from '@hugocxl/sounds';",
      "export const App = () => { play('down'); haptic('light'); return <div className=\"bg-canvas text-ink\"><svg data-icon=\"search\" /><svg data-vector=\"empty-inbox\" /></div>; };",
    ].join('\n'),
    'src/app.css': '@import "@hugocxl/design-system/tailwind";\n:root { --brand: #fe9369; }\n.card { color: var(--ds-ink); }\n',
  });
  assert.deepEqual(result, []);
});

test('unknown icons, styles and exports are errors', async () => {
  const result = await findings({
    'src/a.tsx': [
      "import { GearIcon } from '@hugocxl/icons/react';",
      "import { GithubIcon } from '@hugocxl/icons/react/stroke';",
      "import { SearchIcon } from '@hugocxl/icons/react/stroke/serch';",
      "import { GithubIcon as G } from '@hugocxl/icons/react/solid/github';",
      "import { TrashIcon } from '@hugocxl/icons/react/stroke/search';",
      "import x from '@hugocxl/icons/svg/search';",
      '<svg data-icon="cog" />',
    ].join('\n'),
  });
  assert.deepEqual(rules(result), Array(7).fill('unknown-icon'));
  assert.deepEqual(result.map(finding => finding.line), [1, 2, 3, 4, 5, 6, 7]);
  assert.match(result[0].message, /GearIcon/);
  assert.match(result[1].message, /no stroke style/);
  assert.match(result[4].message, /exports SearchIcon, not TrashIcon/);
  assert.ok(result.every(finding => finding.level === 'error'));
});

test('unknown vectors are errors', async () => {
  const result = await findings({
    'src/a.tsx': "import { HappyVector } from '@hugocxl/vectors/react';\nimport { X } from '@hugocxl/vectors/react/empty-inbox';\nimport y from '@hugocxl/vectors/js/sad';\n<svg data-vector=\"rocket\" />\n",
  });
  assert.deepEqual(rules(result), Array(4).fill('unknown-vector'));
});

test('unknown sounds and haptics are errors only where the library is used', async () => {
  const result = await findings({
    'src/a.ts': "import { play, haptic } from '@hugocxl/sounds';\nplay('click');\nhaptic('buzz');\nplay('up');\n",
    'src/video.ts': "player.play('intro');\n",
  });
  assert.deepEqual(result.map(f => [f.rule, f.file, f.line]), [['unknown-sound', 'src/a.ts', 2], ['unknown-sound', 'src/a.ts', 3]]);
});

test('other icon libraries are errors, in code and in package.json', async () => {
  const result = await findings(
    { 'src/a.tsx': "import { Camera } from 'lucide-react';\nimport { FaBeer } from 'react-icons/fa';\nconst h = require('@heroicons/react/24/solid');\n" },
    { manifest: { dependencies: { '@phosphor-icons/react': '2.0.0' } } },
  );
  assert.deepEqual(result.map(f => [f.rule, f.file]), [
    ['foreign-icons', 'package.json'], ['foreign-icons', 'src/a.tsx'], ['foreign-icons', 'src/a.tsx'], ['foreign-icons', 'src/a.tsx'],
  ]);
});

test('importing a library that is not installed is an error', async () => {
  const result = await findings({ 'src/a.ts': "import { play } from '@hugocxl/sounds';\n" }, { libraries: ['icons'] });
  assert.deepEqual(rules(result), ['missing-library']);
});

test('Tailwind palette and raw colors are warnings next to the design system', async () => {
  const result = await findings({
    'src/a.tsx': '<div className="bg-blue-500 hover:text-gray-700/50 text-white bg-canvas text-red" />',
    'src/a.css': '.a { color: #333; border-color: rgb(0 0 0 / 10%); }\n',
  });
  assert.deepEqual(result.map(f => [f.rule, f.level]), [
    ['raw-color', 'warning'], ['raw-color', 'warning'],
    ['tailwind-palette', 'warning'], ['tailwind-palette', 'warning'], ['tailwind-palette', 'warning'],
  ]);
});

test('without the design system, colors are not checked', async () => {
  const result = await findings({ 'src/a.tsx': '<div className="bg-blue-500" />', 'src/a.css': '.a { color: #333 }' }, { libraries: ['icons'] });
  assert.deepEqual(result, []);
});

test('rules, ignored paths and comments can silence findings', async () => {
  const result = await findings(
    {
      'src/a.tsx': '<div className="bg-blue-500" />\n<svg data-icon="nope" /> {/* stack-ignore */}\n// stack-ignore-next-line\n<svg data-icon="nope" />\n',
      'legacy/old.tsx': "import { Camera } from 'lucide-react';\n",
    },
    { manifest: { stack: { rules: { 'tailwind-palette': 'off', 'unknown-icon': 'warning' }, ignore: ['legacy/**'] } } },
  );
  assert.deepEqual(result, []);
});

test('generated and dependency folders are never checked', async () => {
  const result = await findings({ 'dist/a.js': "import 'lucide';", '.next/b.js': "import 'lucide';", 'node_modules/x/c.js': "import 'lucide';" });
  assert.deepEqual(result, []);
});

test('agent files that are missing or stale are errors, and CLAUDE.md is flagged', async () => {
  const root = project({ files: { 'CLAUDE.md': '@AGENTS.md\n' } });
  const before = (await check(root)).findings;
  assert.ok(before.some(f => f.rule === 'no-claude-md'));
  sync(root);
  const after = (await check(root)).findings;
  assert.deepEqual(rules(after), ['no-claude-md']);
});

test('import parsing covers the module syntaxes', () => {
  const found = importsOf([
    "import A, { B, type C, D as E } from 'a';",
    "import type { F } from 'b';",
    "export { G } from 'c';",
    "import * as H from 'd';",
    "import 'e';",
    "const i = require('f');",
    "const j = await import('g');",
    '@import "h";',
  ].join('\n'));
  assert.deepEqual(found.map(f => f.specifier).sort(), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']);
  assert.deepEqual(found.find(f => f.specifier === 'a').names, ['B', 'C', 'D']);
});

test('globs match relative paths', () => {
  assert.ok(globToRegExp('legacy/**').test('legacy/a/b.tsx'));
  assert.ok(globToRegExp('**/*.test.tsx').test('src/a/b.test.tsx'));
  assert.ok(globToRegExp('src/*.css').test('src/a.css'));
  assert.ok(!globToRegExp('src/*.css').test('src/a/b.css'));
});
