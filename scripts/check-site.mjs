#!/usr/bin/env node
// Check the built site: links, anchors, assets and the design system's page contract.
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, join } from 'node:path';
import assert from 'node:assert/strict';
import { JSDOM } from 'jsdom';

// The design system is copied verbatim from @hugocxl/design-system.
const system = join(dirname(createRequire(import.meta.url).resolve('@hugocxl/design-system/package.json')), 'system');
for (const path of readdirSync(system, { recursive: true }).filter(path => statSync(join(system, path)).isFile())) {
  assert.ok(readFileSync(join(system, path)).equals(readFileSync(`_site/system/${path}`)), `_site/system/${path} differs from the package`);
}

// Inline icons and vectors, as DESIGN.md writes them, keyed by name.
const svgInner = svg => JSDOM.fragment(svg.trim()).firstElementChild.innerHTML.replace(/>\s+</g, '><').trim();
const iconCache = new Map();
const packageIcon = async name => {
  if (!iconCache.has(name)) iconCache.set(name, svgInner(Object.values(await import(`@hugocxl/icons/js/stroke/${name}`))[0]));
  return iconCache.get(name);
};
let icons = 0;
let vectors = 0;

const pages = { 'index.html': 'plain', 'browse.html': 'plain', 'docs.html': 'plain' };
const docs = new Map(Object.keys(pages).map(name => [name, new JSDOM(readFileSync(`_site/${name}`, 'utf8')).window.document]));
const catalog = JSON.parse(readFileSync('packages/vectors/dist/catalog.json', 'utf8'));
const names = new Set(catalog.map(item => item.name));
let links = 0;

for (const [name, doc] of docs) {
  // Page shell from the design system.
  assert.equal(doc.body.className, 'ds', `${name}: body class`);
  assert.equal(doc.body.dataset.layout, pages[name], `${name}: layout`);
  assert.ok(doc.querySelector('head link[rel=stylesheet][href="system/ds.css"]'), `${name}: ds.css`);
  assert.ok(doc.querySelector('head script[src="system/theme.js"]:not([type])'), `${name}: theme.js`);
  assert.ok(doc.querySelector('head script[type=module][src="system/ds.js"]'), `${name}: ds.js`);
  assert.equal(doc.body.firstElementChild.className, 'ds-masthead', `${name}: masthead first`);
  assert.deepEqual([...doc.querySelectorAll('.ds-masthead a')].map(a => a.textContent), ['@hugocxl/vectors', 'Browse', 'Docs', 'GitHub']);
  assert.ok(doc.querySelector('.ds-masthead [data-ds-theme]'), `${name}: theme button`);
  assert.deepEqual([...doc.querySelectorAll('.ds-footer a')].map(a => a.textContent),
    ['Icons', 'Vectors', 'Design system', 'npm', 'License', '@hugocxl'], `${name}: footer`);
  assert.equal(doc.querySelectorAll('h1').length, 1, `${name}: one h1`);
  assert.ok(doc.querySelectorAll('.ds-accent, .ds-dot').length <= 2, `${name}: accent budget`);
  assert.ok(doc.querySelectorAll('.ds-button').length <= 1, `${name}: one filled button`);
  for (const svg of doc.querySelectorAll('svg.ds-icon')) {
    const icon = svg.dataset.icon;
    assert.ok(icon, `${name}: icon without data-icon`);
    assert.equal(svg.getAttribute('viewBox'), '0 0 16 16', `${name}: ${icon} viewBox`);
    assert.equal(svg.getAttribute('fill'), 'none', `${name}: ${icon} fill`);
    assert.equal(svg.getAttribute('aria-hidden'), 'true', `${name}: ${icon} aria-hidden`);
    assert.equal(svg.innerHTML.replace(/>\s+</g, '><').trim(), await packageIcon(icon), `${name}: ${icon} differs from @hugocxl/icons`);
    icons++;
  }
  assert.equal(doc.querySelectorAll('svg:not(.ds-icon):not(.ds-vector)').length, 0, `${name}: stray inline svg`);
  for (const svg of doc.querySelectorAll('svg.ds-vector')) {
    const vector = svg.dataset.vector;
    assert.ok(names.has(vector), `${name}: unknown vector ${vector}`);
    assert.equal(svg.innerHTML.replace(/>\s+</g, '><').trim(), svgInner(readFileSync(`figures/${vector}.svg`, 'utf8')), `${name}: ${vector} differs from figures/`);
    vectors++;
    assert.ok(!svg.hasAttribute('color'), `${name}: vector keeps a color attribute`);
    assert.ok(svg.querySelector('title')?.textContent && svg.querySelector('desc')?.textContent, `${name}: vector title/desc`);
  }
  for (const id of [...doc.querySelectorAll('[id]')].map(element => element.id)) {
    assert.equal(doc.querySelectorAll(`[id="${id}"]`).length, 1, `${name}: duplicate id ${id}`);
  }

  // Links, anchors and assets.
  for (const a of doc.querySelectorAll('a[href]')) {
    const href = a.getAttribute('href');
    if (/^(https?:|mailto:)/.test(href)) continue;
    links++;
    const [path, hash] = href.split('#');
    const target = path === './' || path === '' && name === 'index.html' ? 'index.html' : path || name;
    assert.ok(existsSync(`_site/${target}`), `${name}: missing ${href}`);
    if (hash) assert.ok(docs.get(target)?.getElementById(decodeURIComponent(hash)), `${name}: missing anchor ${href}`);
  }
  for (const element of doc.querySelectorAll('[src], link[href]')) {
    const path = element.getAttribute('src') || element.getAttribute('href');
    if (!/^https?:/.test(path)) assert.ok(existsSync(`_site/${path}`), `${name}: missing asset ${path}`);
  }
}
for (const asset of ['system/fonts/Geist-Variable.woff2', 'system/fonts/GeistMono-Variable.woff2', 'system/images/gray-folds.png']) {
  assert.ok(existsSync(`_site/${asset}`), `missing ${asset}`);
}

// Home: recipe order, real vectors and real numbers.
const home = docs.get('index.html');
const order = [...home.querySelector('article').children].map(element =>
  element.matches('.ds-statement') ? 'statement' : element.matches('.ds-meta') ? 'meta' :
  element.matches('.ds-section') ? 'section' : element.matches('figure.ds-wide') ? 'figure-wide' :
  element.matches('.ds-button') ? 'button' : element.tagName).join(' ');
assert.match(order, /^statement meta section figure-wide( section)* button$/, `home order: ${order}`);
assert.equal(home.querySelectorAll('.ds-media > svg.ds-vector').length, 1);
assert.match(home.querySelector('.ds-meta').textContent, new RegExp(catalog.length.toLocaleString('en-US')));
assert.equal(home.querySelector('.ds-button').getAttribute('href'), 'browse.html');
const accent = home.querySelector('.ds-statement .ds-accent').textContent.trim().split(/\s+/).length;
assert.ok(accent >= 2 && accent <= 3, 'accent phrase is two or three words');
for (const { name } of JSON.parse(home.getElementById('home-figures').textContent)) assert.ok(names.has(name), name);

// Browse: every vector listed once, deep links resolve, data matches the catalog.
const browse = docs.get('browse.html');
const items = [...browse.querySelectorAll('#results > li')];
assert.equal(items.length, catalog.length);
assert.deepEqual(items.map(li => li.id), catalog.map(item => item.name));
for (const li of items) assert.equal(li.querySelector('a').getAttribute('href'), `#${li.id}`);
for (const item of catalog) assert.ok(existsSync(`_site/figures/${item.name}.svg`), item.name);
assert.equal(JSON.parse(browse.getElementById('browse-data').textContent).length, catalog.length);
assert.equal(browse.querySelectorAll('[data-category]').length, new Set(catalog.map(item => item.category)).size + 1);
assert.ok(browse.querySelector('label[for="browse-query"]'), 'search has a visible label');

// Docs: every h2 of USAGE.md is a section with an id, code and tables use system markup.
const guide = docs.get('docs.html');
const headings = [...readFileSync('docs/USAGE.md', 'utf8').matchAll(/^## (.+)$/gm)].map(match => match[1]);
assert.deepEqual([...guide.querySelectorAll('.ds-section > h2')].map(h2 => h2.textContent), headings);
assert.equal(guide.querySelectorAll('pre:not(.ds-code pre)').length, 0);
assert.equal(guide.querySelectorAll('table:not(.ds-table)').length, 0);
for (const table of guide.querySelectorAll('table')) assert.ok(table.parentElement.matches('.ds-table-scroll[tabindex="0"]'));
for (const code of guide.querySelectorAll('.ds-code')) assert.equal(code.querySelector('button').textContent, 'Copy');

console.log(`Site verified: 3 pages, ${links} internal links, ${icons} icons, ${vectors} inline vectors, ${items.length} vectors, ${headings.length} guide sections.`);
