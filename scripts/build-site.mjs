#!/usr/bin/env node
// Build the website from website/, docs/USAGE.md and the generated catalog into _site/.
// The design system and the interface icons come from the @hugocxl/design-system and
// @hugocxl/icons packages; the vectors are this repo's own figures/.
import { cpSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname } from 'node:path';
import { marked } from 'marked';

const require = createRequire(import.meta.url);
const designSystem = dirname(require.resolve('@hugocxl/design-system/package.json'));

const out = '_site';
const site = 'https://hugocxl.github.io/vectors/';
const repo = 'https://github.com/hugocxl/vectors';
const read = path => readFileSync(path, 'utf8');
const escape = text => String(text).replace(/[&<>"]/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[char]);
const number = value => value.toLocaleString('en-US');

const catalog = JSON.parse(read('packages/vectors/dist/catalog.json'));
const categories = [...new Map(catalog.map(item => [item.categoryId, item.category])).entries()]
  .sort((a, b) => a[1].localeCompare(b[1]));
const count = number(catalog.length);

rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });
cpSync(`${designSystem}/system`, `${out}/system`, { recursive: true });
cpSync('figures', `${out}/figures`, { recursive: true });
for (const file of ['site.css', 'home.js', 'browse.js']) cpSync(`website/${file}`, `${out}/${file}`);
writeFileSync(`${out}/.nojekyll`, '');

// An inline vector for the design system's figure slots: ink, 4:3, title and desc kept.
const inlineVector = name => read(`figures/${name}.svg`)
  .replace(' xmlns="http://www.w3.org/2000/svg"', ` class="ds-vector" data-vector="${name}"`)
  .replace(/ color="[^"]*"/, '')
  .trim();

// An inline stroke icon from @hugocxl/icons, as DESIGN.md writes it.
const icons = new Map();
for (const file of ['index.html', 'browse.html', 'docs.html']) {
  for (const [, name] of read(`website/${file}`).matchAll(/{{icon ([\w-]+)}}/g)) icons.set(name, null);
}
icons.set('contrast', null);
for (const name of icons.keys()) {
  const svg = Object.values(await import(`@hugocxl/icons/js/stroke/${name}`))[0];
  const inner = svg.trim().replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '').split('\n').map(line => line.trim()).join('');
  icons.set(name, `<svg class="ds-icon" data-icon="${name}" viewBox="0 0 16 16" fill="none" aria-hidden="true">${inner}</svg>`);
}
const icon = name => icons.get(name);

const masthead = `  <header class="ds-masthead">
    <a class="ds-wordmark" href="./">@hugocxl/vectors</a>
    <a href="browse.html">Browse</a>
    <a href="docs.html">Docs</a>
    <a href="${repo}">GitHub</a>
    <button class="ds-theme" type="button" data-ds-theme aria-label="Switch theme">${icon('contrast')}</button>
  </header>`;
const footer = `  <footer class="ds-footer">
    <ul><li><a href="https://hugocxl.github.io/icons/">Icons</a></li><li><a href="${site}">Vectors</a></li><li><a href="https://hugocxl.github.io/design-system/">Design system</a></li></ul>
    <ul><li><a href="https://www.npmjs.com/package/@hugocxl/vectors">npm</a></li><li><a href="${repo}/blob/main/LICENSE">License</a></li><li><a href="https://github.com/hugocxl">@hugocxl</a></li></ul>
  </footer>`;
const head = (title, description, file) => `  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>${escape(title)}</title>
  <meta name="description" content="${escape(description)}">
  <link rel="canonical" href="${site}${file === 'index.html' ? '' : file}">
  <link rel="stylesheet" href="system/ds.css">
  <link rel="stylesheet" href="site.css">
  <script src="system/theme.js"></script>
  <script type="module" src="system/ds.js"></script>`;

function page(file, values) {
  let html = read(`website/${file}`).replace(/{{icon ([\w-]+)}}/g, (_, name) => icon(name));
  for (const [key, value] of Object.entries({ masthead, footer, count, categories: categories.length, ...values })) {
    html = html.replaceAll(`{{${key}}}`, () => String(value));
  }
  const missing = html.match(/{{\w+}}/);
  if (missing) throw new Error(`${file}: unfilled placeholder ${missing[0]}`);
  writeFileSync(`${out}/${file}`, html);
}

// Home.
const homeFigures = ['modular-design', 'product-launch', 'collaboration', 'ai-assistant', 'checkout', 'empty-inbox']
  .map(name => catalog.find(item => item.name === name))
  .map(({ name, title }) => ({ name, title }));
page('index.html', {
  head: head('Vectors', `${count} isometric line illustrations for websites and apps, for SVG, JavaScript, React, React Native and Swift.`, 'index.html'),
  figure: inlineVector(homeFigures[0].name),
  figureTitle: escape(homeFigures[0].title),
  figures: JSON.stringify(homeFigures),
});

// Browse.
const filters = categories.map(([id, title]) =>
  `          <button type="button" class="ds-label" data-category="${id}" aria-pressed="false">${escape(title)}</button>`).join('\n');
const items = catalog.map(item =>
  `        <li id="${item.name}"><a href="#${item.name}"><span class="browse-art"></span><span>${escape(item.title)}</span></a></li>`).join('\n');
const data = catalog.map(({ name, export: symbol, title, description, category, categoryId, placement }) =>
  ({ name, export: symbol, title, description, category, categoryId, placement }));
page('browse.html', {
  head: head('Browse vectors — Vectors', `Search ${count} isometric line illustrations by name, category and use case, then copy or download the SVG.`, 'browse.html'),
  filters,
  items,
  data: JSON.stringify(data).replaceAll('</', '<\\/'),
});

// Docs, rendered from docs/USAGE.md with the design system's section, code and table markup.
const slug = text => text.toLowerCase().replace(/<[^>]+>/g, '').replace(/[^\w\s-]/g, '').trim().replace(/\s+/g, '-');
const markdown = read('docs/USAGE.md').replace(/\]\(\.\.\/([^)]+)\)/g, `](${repo}/blob/main/$1)`);
const [, title, body] = markdown.match(/^# (.+)\n([\s\S]*)$/);
const renderer = new marked.Renderer();
renderer.code = ({ text }) => `<div class="ds-code"><pre tabindex="0"><code>${escape(text)}</code></pre><button type="button">Copy</button></div>\n`;
renderer.table = function (token) {
  const cell = (c, header, scope) => {
    const tag = header || scope ? 'th' : 'td';
    const attr = header ? ' scope="col"' : scope ? ' scope="row"' : '';
    return `<${tag}${attr}>${this.parser.parseInline(c.tokens)}</${tag}>`;
  };
  const headRow = `<tr>${token.header.map(c => cell(c, true)).join('')}</tr>`;
  const rows = token.rows.map(row => `<tr>${row.map((c, i) => cell(c, false, i === 0)).join('')}</tr>`).join('\n');
  return `<div class="ds-table-scroll" tabindex="0">\n<table class="ds-table">\n<thead>${headRow}</thead>\n<tbody>\n${rows}\n</tbody>\n</table>\n</div>\n`;
};
const sections = body.split(/^## /m);
const lead = sections.shift();
const content = [
  `      <section class="ds-section">\n${marked.parse(lead, { renderer })}      </section>`,
  ...sections.map(section => {
    const [heading, ...rest] = section.split('\n');
    return `      <section class="ds-section" id="${slug(heading)}">\n        <h2>${marked.parseInline(heading)}</h2>\n${marked.parse(rest.join('\n'), { renderer })}      </section>`;
  }),
].join('\n');
page('docs.html', {
  head: head('Docs — Vectors', 'Install and use Vectors on the web, in React and React Native, and in SwiftUI, UIKit and AppKit.', 'docs.html'),
  title: escape(title),
  content,
});

console.log(`Built _site with ${count} vectors in ${categories.length} categories.`);
