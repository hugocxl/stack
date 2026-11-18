#!/usr/bin/env node
// Build the website from website/, docs/USAGE.md and the generated catalog into _site/.
import { cpSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { marked } from 'marked';

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
cpSync('website/system', `${out}/system`, { recursive: true });
cpSync('figures', `${out}/figures`, { recursive: true });
for (const file of ['site.css', 'home.js', 'browse.js']) cpSync(`website/${file}`, `${out}/${file}`);
writeFileSync(`${out}/.nojekyll`, '');

// An inline vector for the design system's figure slots: ink, 4:3, title and desc kept.
const inlineVector = name => read(`figures/${name}.svg`)
  .replace(' xmlns="http://www.w3.org/2000/svg"', ' class="p9-vector"')
  .replace(/ color="[^"]*"/, '')
  .trim();

const masthead = `  <header class="p9-masthead">
    <a class="p9-wordmark" href="./">@hugocxl/vectors</a>
    <a href="browse.html">Browse</a>
    <a href="docs.html">Docs</a>
    <a href="${repo}">GitHub</a>
    <button class="p9-theme" type="button" data-p9-theme aria-label="Switch theme"><svg class="p9-icon" data-icon="contrast" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M1.375 8Q1.375 6.6526 1.8959 5.4211Q2.3988 4.232 3.3154 3.3154Q4.232 2.3988 5.4211 1.8959Q6.6526 1.375 8 1.375Q9.3474 1.375 10.5789 1.8959Q11.768 2.3988 12.6846 3.3154Q13.6012 4.232 14.1041 5.4211Q14.625 6.6526 14.625 8Q14.625 9.3474 14.1041 10.5789Q13.6012 11.768 12.6846 12.6846Q11.768 13.6012 10.5789 14.1041Q9.3474 14.625 8 14.625Q6.6526 14.625 5.4211 14.1041Q4.232 13.6012 3.3154 12.6846Q2.3988 11.768 1.8959 10.5789Q1.375 9.3474 1.375 8ZM2.625 8Q2.625 9.094 3.0471 10.092Q3.4551 11.0565 4.1993 11.8007Q4.9435 12.5449 5.908 12.9529Q6.906 13.375 8 13.375L8 2.625Q6.906 2.625 5.908 3.0471Q4.9435 3.4551 4.1993 4.1993Q3.4551 4.9435 3.0471 5.908Q2.625 6.906 2.625 8Z" fill="currentColor"/></svg></button>
  </header>`;
const footer = `  <footer class="p9-footer">
    <ul><li><a href="https://hugocxl.github.io/icons/">Icons</a></li><li><a href="${site}">Vectors</a></li><li><a href="https://hugocxl.github.io/design-system/">Design system</a></li></ul>
    <ul><li><a href="https://www.npmjs.com/package/@hugocxl/vectors">npm</a></li><li><a href="${repo}/blob/main/LICENSE">License</a></li><li><a href="https://github.com/hugocxl">@hugocxl</a></li></ul>
  </footer>`;
const head = (title, description, file) => `  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>${escape(title)}</title>
  <meta name="description" content="${escape(description)}">
  <link rel="canonical" href="${site}${file === 'index.html' ? '' : file}">
  <link rel="stylesheet" href="system/p9.css">
  <link rel="stylesheet" href="site.css">
  <script src="system/theme.js"></script>
  <script type="module" src="system/p9.js"></script>`;

function page(file, values) {
  let html = read(`website/${file}`);
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
  `          <button type="button" class="p9-label" data-category="${id}" aria-pressed="false">${escape(title)}</button>`).join('\n');
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
renderer.code = ({ text }) => `<div class="p9-code"><pre tabindex="0"><code>${escape(text)}</code></pre><button type="button">Copy</button></div>\n`;
renderer.table = function (token) {
  const cell = (c, header, scope) => {
    const tag = header || scope ? 'th' : 'td';
    const attr = header ? ' scope="col"' : scope ? ' scope="row"' : '';
    return `<${tag}${attr}>${this.parser.parseInline(c.tokens)}</${tag}>`;
  };
  const headRow = `<tr>${token.header.map(c => cell(c, true)).join('')}</tr>`;
  const rows = token.rows.map(row => `<tr>${row.map((c, i) => cell(c, false, i === 0)).join('')}</tr>`).join('\n');
  return `<div class="p9-table-scroll" tabindex="0">\n<table class="p9-table">\n<thead>${headRow}</thead>\n<tbody>\n${rows}\n</tbody>\n</table>\n</div>\n`;
};
const sections = body.split(/^## /m);
const lead = sections.shift();
const content = [
  `      <section class="p9-section">\n${marked.parse(lead, { renderer })}      </section>`,
  ...sections.map(section => {
    const [heading, ...rest] = section.split('\n');
    return `      <section class="p9-section" id="${slug(heading)}">\n        <h2>${marked.parseInline(heading)}</h2>\n${marked.parse(rest.join('\n'), { renderer })}      </section>`;
  }),
].join('\n');
page('docs.html', {
  head: head('Docs — Vectors', 'Install and use Vectors on the web, in React and React Native, and in SwiftUI, UIKit and AppKit.', 'docs.html'),
  title: escape(title),
  content,
});

console.log(`Built _site with ${count} vectors in ${categories.length} categories.`);
