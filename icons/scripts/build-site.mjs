// Build the GitHub Pages site from website/ into _site/.
// Pages follow the design system from the @hugocxl/design-system package; the icons come from this repository.
import { cpSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, join } from "node:path";
import { marked } from "marked";
import { defaultColor } from "@hugocxl/icons/colors";

const out = "_site";
const designSystem = dirname(createRequire(import.meta.url).resolve("@hugocxl/design-system/package.json"));
const read = (path) => readFileSync(path, "utf8");
const escape = (text) =>
  String(text).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const number = new Intl.NumberFormat("en");

const catalog = JSON.parse(read("catalog.json"));
const { version } = JSON.parse(read("packages/icons/package.json"));
const STYLES = ["duotone", "solid", "stroke"];
const source = (name, style) => (style === "duotone" ? `icons/${name}.svg` : `icons/styles/${style}/${name}.svg`);
const categories = [...new Set(catalog.map((icon) => icon.category))].sort();
const facts = {
  count: number.format(catalog.length),
  styles: String(STYLES.length),
  full: number.format(catalog.filter((icon) => icon.styles.length === STYLES.length).length),
  brands: number.format(catalog.filter((icon) => icon.category === "Brands").length),
  "category-count": String(categories.length),
  version,
};

// Inline artwork renders in ink through currentColor.
const svg = (name, style, attributes = 'aria-hidden="true" focusable="false"') =>
  read(source(name, style)).trim().replace("<svg ", `<svg ${attributes} `);
const strokeIcon = (name) => svg(name, "stroke", 'class="ds-icon" aria-hidden="true" focusable="false"');

const specimenNames = [
  "home", "search", "heart", "star", "bell", "calendar",
  "camera", "music", "cloud", "folder", "mail", "message-circle",
  "settings", "globe", "map-pin", "sun", "moon", "zap",
  "coffee", "gift", "bookmark", "clock", "compass", "sparkles",
];
const specimen = STYLES.map((style, index) => {
  const name = style[0].toUpperCase() + style.slice(1);
  const caption = `Fig. ${String(index + 1).padStart(2, "0")} / ${name}`;
  return `<div class="site-specimen" data-style="${style}" data-caption="${caption}" role="img" aria-label="${specimenNames.length} icons in the ${name} style"${index ? " hidden" : ""}>${specimenNames.map((icon) => svg(icon, style)).join("")}</div>`;
}).join("");

// ─── Docs: docs/USAGE.md rendered into P9 sections ─────────────────────
const slug = (text) => text.toLowerCase().replace(/[^\w\s-]/g, "").replace(/\s/g, "-");
const github = "https://github.com/hugocxl/stack/blob/main/icons/";
const renderer = new marked.Renderer();
renderer.code = ({ text }) =>
  `<div class="ds-code"><pre tabindex="0"><code>${escape(text)}</code></pre><button type="button">Copy</button></div>\n`;
const baseTable = renderer.table.bind(renderer);
renderer.table = (token) =>
  `<div class="ds-table-scroll" tabindex="0">${baseTable(token).replace("<table>", '<table class="ds-table">')}</div>\n`;
renderer.heading = function ({ tokens, depth }) {
  return `<h${depth}>${this.parser.parseInline(tokens)}</h${depth}>\n`;
};
renderer.link = function ({ href, title, tokens }) {
  const target = href
    .replace(/^\.\.\/docs\/CATALOG\.md$/, `${github}docs/CATALOG.md`)
    .replace(/^\.\.\/(.+)$/, `${github}$1`)
    .replace(/^(LICENSE|NOTICE|THIRD_PARTY_LICENSES\.md)$/, `${github}$1`);
  return `<a href="${escape(target)}"${title ? ` title="${escape(title)}"` : ""}>${this.parser.parseInline(tokens)}</a>`;
};

const tokens = marked.lexer(read("docs/USAGE.md"));
let docsTitle = "Docs";
const groups = [{ id: null, heading: null, tokens: [] }];
for (const token of tokens) {
  if (token.type === "heading" && token.depth === 1) docsTitle = token.text;
  else if (token.type === "heading" && token.depth === 2) groups.push({ id: slug(token.text), heading: token, tokens: [] });
  else groups.at(-1).tokens.push(token);
}
const docs = groups
  .filter((group) => group.heading || group.tokens.some((token) => token.type !== "space"))
  .map((group) => {
    const body = marked.parser(Object.assign(group.tokens, { links: tokens.links }), { renderer });
    const heading = group.heading ? `<h2>${marked.parseInline(group.heading.text)}</h2>\n` : "";
    return `      <section class="ds-section"${group.id ? ` id="${group.id}"` : ""}>\n${heading}${body}      </section>`;
  })
  .join("\n");

// ─── Browser data ───────────────────────────────────────────────────────
const categoryButtons = ["All", ...categories]
  .map(
    (category) =>
      `            <button type="button" data-category="${escape(category)}" aria-pressed="${category === "All"}">${escape(category)} <span>${number.format(category === "All" ? catalog.length : catalog.filter((icon) => icon.category === category).length)}</span></button>`,
  )
  .join("\n");
const browseData = JSON.stringify(
  catalog.map((icon) => [icon.name, icon.category, icon.tags.join(" "), icon.styles.length === STYLES.length ? 1 : 0, icon.defaultColor]),
).replaceAll("</", "<\\/");

// ─── Templates ──────────────────────────────────────────────────────────
const partial = (name) => read(`website/partials/${name}.html`).replace(/\n$/, "");
function render(template, values) {
  const html = template
    .replace(/\{\{([\w-]+)\}\}/g, (match, key) => (key in values ? values[key] : match))
    .replace(/\{\{head ([^}]*)\}\}/, (_, args) => {
      const attributes = Object.fromEntries([...args.matchAll(/(\w+)="([^"]*)"/g)].map((m) => [m[1], m[2]]));
      return partial("head").replace(/\{\{(\w+)\}\}/g, (__, key) => attributes[key] ?? "");
    })
    .replace("{{masthead}}", partial("masthead"))
    .replace("{{footer}}", partial("footer"))
    .replace(/\{\{icon ([\w-]+)\}\}/g, (_, name) => strokeIcon(name));
  const unknown = html.match(/\{\{[^}]*\}\}/);
  if (unknown) throw new Error(`Unknown template value ${unknown[0]}`);
  return html;
}

rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });
cpSync(join(designSystem, "system"), `${out}/system`, { recursive: true });
for (const file of ["site.css", "home.js", "browse.js"]) cpSync(`website/${file}`, `${out}/${file}`);
for (const style of STYLES) {
  cpSync(style === "duotone" ? "icons" : `icons/styles/${style}`, `${out}/svg/${style}`, {
    recursive: true,
    filter: (path) => !path.endsWith(".DS_Store") && (style !== "duotone" || !path.startsWith("icons/styles")),
  });
  const colored = `${out}/svg/colored/${style}`;
  mkdirSync(colored, { recursive: true });
  for (const icon of catalog.filter(icon => icon.defaultColor && icon.styles.includes(style))) {
    const light = defaultColor(icon.name, "light");
    const color = defaultColor(icon.name);
    const attributes = `color="${light}" style="color-scheme: light dark; color: ${color}"`;
    writeFileSync(`${colored}/${icon.name}.svg`, svg(icon.name, style, attributes) + "\n");
  }
}

const values = { ...facts, specimen, categories: categoryButtons, catalog: browseData, docs, "docs-title": escape(docsTitle) };
for (const page of ["index.html", "browse.html", "docs.html"]) {
  writeFileSync(`${out}/${page}`, render(read(`website/${page}`), values));
}

// Old addresses keep working.
const redirect = (from, to, label) =>
  writeFileSync(
    `${out}/${from}`,
    `<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>${label} · Icons</title>\n<link rel="canonical" href="https://hugocxl.github.io/stack/icons/${to}">\n<script>location.replace('${to}' + location.hash);</script>\n<meta http-equiv="refresh" content="0;url=${to}">\n</head><body><a href="${to}">${label}</a></body></html>\n`,
  );
redirect("icons.html", "browse.html", "Browse the icons");
redirect("guide.html", "docs.html", "Read the docs");
writeFileSync(`${out}/.nojekyll`, "");
console.log(`Built site with ${facts.count} icons in ${STYLES.length} styles.`);
