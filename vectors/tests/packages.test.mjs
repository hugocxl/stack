import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import * as vectors from '../packages/vectors/dist/react/index.js';

const files = readdirSync('figures').filter(file => file.endsWith('.svg')).sort();
const symbol = file => file.slice(0, -4).split('-').map(part => part[0].toUpperCase() + part.slice(1)).join('') + 'Vector';
const text = (source, tag) => source.match(new RegExp(`<${tag}>([^<]*)</${tag}>`))[1];
const unescape = value => value.replaceAll('&amp;', '&').replaceAll('&lt;', '<').replaceAll('&gt;', '>').replaceAll('&quot;', '"').replaceAll('&#x27;', "'");

test('every vector renders with its geometry, opacities, title and description', () => {
  assert.equal(files.length, 2000);
  assert.equal(Object.keys(vectors).length, files.length);
  for (const file of files) {
    const source = readFileSync(`figures/${file}`, 'utf8');
    const rendered = renderToStaticMarkup(createElement(vectors[symbol(file)], { size: 240, color: 'red' }));
    assert.ok(rendered.includes('width="240"') && rendered.includes('height="180"'), file);
    assert.ok(rendered.includes('color="red"'), file);
    assert.ok(rendered.includes('role="img"'), file);
    assert.equal(unescape(text(rendered, 'title')), unescape(text(source, 'title')), file);
    assert.equal(unescape(text(rendered, 'desc')), unescape(text(source, 'desc')), file);
    for (const match of source.matchAll(/(?:viewBox|d|stroke-opacity)="[^"]*"/g)) {
      assert.ok(rendered.includes(match[0]), `${file}: ${match[0].slice(0, 40)}`);
    }
    assert.ok(!rendered.includes('vector-effect'), `${file}: strokes scale with the artwork`);
    assert.ok(rendered.includes('stroke-width="3.6"'), file);
  }
});

test('web components default to currentColor at 480 x 360 and accept overrides', () => {
  const render = props => renderToStaticMarkup(createElement(vectors.ModularDesignVector, props));
  assert.match(render({}), /width="480" height="360"/);
  assert.match(render({}), /color="currentColor"/);
  assert.doesNotMatch(render({}), /#8792a2/);
  assert.doesNotMatch(render({}), /aria-hidden/);
  assert.match(render({ 'aria-hidden': true }), /aria-hidden="true"/);
  assert.match(render({ 'aria-label': 'Modules' }), /aria-label="Modules"/);
  assert.match(render({ size: 240, width: 320 }), /width="320" height="180"/);
  assert.match(render({ className: 'hero' }), /class="hero"/);
});

test('package entry points and per-vector imports resolve', async () => {
  const root = await import('@hugocxl/vectors/react');
  const single = await import('@hugocxl/vectors/react/modular-design');
  assert.equal(root.ModularDesignVector, single.ModularDesignVector);
  const manifest = JSON.parse(readFileSync('packages/vectors/package.json'));
  assert.equal(manifest.name, '@hugocxl/vectors');
  assert.equal(manifest.sideEffects, false);
  assert.equal(manifest.exports['.'].default, './dist/js/index.js');
  for (const path of ['.', './js', './js/*', './react', './react/*', './react-native', './react-native/*', './catalog.json', './package.json']) {
    assert.ok(manifest.exports[path], path);
  }
  assert.equal(readFileSync('packages/vectors/LICENSE', 'utf8'), readFileSync('LICENSE', 'utf8'));
});

test('the catalog describes every vector with its category and use case', async () => {
  const { default: catalog } = await import('@hugocxl/vectors/catalog.json', { with: { type: 'json' } });
  assert.equal(catalog.length, files.length);
  assert.deepEqual(catalog.map(item => item.name), files.map(file => file.slice(0, -4)).sort());
  const js = await import('@hugocxl/vectors/js');
  for (const item of catalog) {
    assert.ok(item.title && item.description && item.category && item.categoryId && item.placement, item.name);
    assert.equal(item.export, symbol(`${item.name}.svg`));
    assert.equal(typeof js[item.export], 'string');
  }
  assert.equal(new Set(catalog.map(item => item.category)).size, 23);
});

test('all adapters bundle and tree shake unused vectors', async () => {
  const { build } = await import('esbuild');
  for (const platform of ['js', 'react', 'react-native']) {
    const result = await build({
      stdin: { contents: `export { ModularDesignVector } from '@hugocxl/vectors/${platform}';`, resolveDir: process.cwd() },
      bundle: true,
      write: false,
      format: 'esm',
      external: ['react', 'react-native-svg'],
      metafile: true,
    });
    const output = result.outputFiles[0].text;
    assert.match(output, /ModularDesignVector/);
    assert.doesNotMatch(output, /FastPerformanceVector/);
    const included = Object.entries(Object.values(result.metafile.outputs)[0].inputs)
      .filter(([path, info]) => path.includes('/dist/') && info.bytesInOutput > 0)
      .map(([path]) => path);
    assert.deepEqual(included, [`packages/vectors/dist/${platform}/modular-design.js`]);
  }
});

test('pure JavaScript exports preserve SVGs without framework dependencies', async () => {
  const js = await import('@hugocxl/vectors/js');
  const root = await import('@hugocxl/vectors');
  const single = await import('@hugocxl/vectors/js/modular-design');
  assert.equal(single.ModularDesignVector, js.ModularDesignVector);
  assert.deepEqual(root, js);
  for (const file of files) assert.equal(js[symbol(file)], readFileSync(`figures/${file}`, 'utf8'));
  const manifest = JSON.parse(readFileSync('packages/vectors/package.json'));
  assert.equal(manifest.dependencies, undefined);
  for (const peer of Object.keys(manifest.peerDependencies)) assert.equal(manifest.peerDependenciesMeta[peer].optional, true);
});

test('native components label the image and keep the 4:3 proportions', async () => {
  const source = readFileSync('packages/vectors/dist/react-native/modular-design.js', 'utf8');
  assert.match(source, /from "react-native-svg"/);
  assert.match(source, /accessibilityLabel: "Modular design"/);
  assert.match(source, /height: size \* 360 \/ 480/);
  assert.match(source, /color = "currentColor"/);
  assert.doesNotMatch(source, /xmlns|"role"/);
});
