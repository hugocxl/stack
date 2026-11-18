// Check the built site in _site/: links, anchors, assets and the P9 page contract.
import { existsSync, readFileSync } from "node:fs";
import assert from "node:assert/strict";
import { JSDOM } from "jsdom";

const site = "_site";
const pages = ["index.html", "browse.html", "docs.html"];
const redirects = ["icons.html", "guide.html"];
const catalog = JSON.parse(readFileSync("catalog.json", "utf8"));
const docs = new Map(
  [...pages, ...redirects].map((name) => [name, new JSDOM(readFileSync(`${site}/${name}`, "utf8")).window.document]),
);
const local = (href) => !/^(https?:|mailto:|data:)/.test(href);
let links = 0;

for (const [name, doc] of docs) {
  for (const a of doc.querySelectorAll("a[href]")) {
    const href = a.getAttribute("href");
    if (!local(href)) continue;
    links++;
    const [path, hash] = href.split("#");
    const target = !path || path === "./" ? (path ? "index.html" : name) : path;
    assert.ok(existsSync(`${site}/${target}`), `${name}: missing ${href}`);
    if (hash) assert.ok(docs.get(target)?.getElementById(hash), `${name}: missing anchor ${href}`);
  }
  for (const element of doc.querySelectorAll("[src], link[href]")) {
    const path = (element.getAttribute("src") || element.getAttribute("href")).split(/[?#]/)[0];
    if (local(path)) assert.ok(existsSync(`${site}/${path}`), `${name}: missing asset ${path}`);
  }
}

// Every page is a P9 page with the shared masthead and footer.
const linkList = (root) => [...root.querySelectorAll("a")].map((a) => `${a.textContent.trim()} ${a.getAttribute("href")}`);
const layouts = { "index.html": "plain", "browse.html": "plain", "docs.html": "plain" };
for (const name of pages) {
  const doc = docs.get(name);
  const body = doc.body;
  assert.ok(body.classList.contains("p9"), `${name}: body.p9`);
  assert.equal(body.dataset.layout, layouts[name], `${name}: layout`);
  assert.ok(doc.querySelector('head link[rel=stylesheet][href="system/p9.css"]'), `${name}: p9.css`);
  assert.ok(doc.querySelector('head script[src="system/theme.js"]:not([type])'), `${name}: theme.js`);
  assert.ok(doc.querySelector('head script[type=module][src="system/p9.js"]'), `${name}: p9.js`);
  assert.equal(body.firstElementChild.className, "p9-masthead", `${name}: masthead first`);
  assert.equal(body.lastElementChild.className, "p9-footer", `${name}: footer last`);
  assert.deepEqual(linkList(doc.querySelector(".p9-masthead")), [
    "@hugocxl/icons ./",
    "Browse browse.html",
    "Docs docs.html",
    "GitHub https://github.com/hugocxl/icons",
  ]);
  assert.ok(doc.querySelector(".p9-masthead > button.p9-theme[data-p9-theme]"), `${name}: theme button`);
  assert.deepEqual(linkList(doc.querySelector(".p9-footer")), [
    "Icons https://hugocxl.github.io/icons/",
    "Vectors https://hugocxl.github.io/vectors/",
    "Design system https://hugocxl.github.io/design-system/",
    "npm https://www.npmjs.com/package/@hugocxl/icons",
    "License https://github.com/hugocxl/icons/blob/main/LICENSE",
    "@hugocxl https://github.com/hugocxl",
  ]);
  assert.ok(doc.querySelectorAll(".p9-accent, .p9-dot").length <= 2, `${name}: accent budget`);
  assert.ok(doc.querySelectorAll(".p9-button").length <= 1, `${name}: one filled button`);
  assert.equal(doc.querySelectorAll("main article.p9-column.p9-opening").length, 1, `${name}: one column`);
  for (const svg of doc.querySelectorAll("main svg")) {
    assert.ok(!svg.closest(".p9-accent"), `${name}: icon in accent`);
  }
}

// Home follows the recipe: statement meta section figure section* button.
const home = docs.get("index.html");
const sequence = [...home.querySelector("main article").children].map((el) =>
  el.matches(".p9-statement") ? "statement"
  : el.matches(".p9-meta") ? "meta"
  : el.matches(".p9-section") ? "section"
  : el.matches("figure.p9-wide") ? "figure"
  : el.matches(".p9-button") ? "button"
  : `?${el.tagName}`,
);
assert.match(sequence.join(" "), /^statement meta section figure( section)* button$/, `home order: ${sequence}`);
assert.equal(home.querySelectorAll(".p9-dot").length, 1);
assert.equal(home.querySelectorAll(".p9-accent").length, 1);
assert.match(home.querySelector(".p9-meta").textContent, new RegExp(catalog.length.toLocaleString("en")));
const specimens = home.querySelectorAll(".site-specimen");
assert.equal(specimens.length, 3);
for (const specimen of specimens) assert.equal(specimen.querySelectorAll("svg").length, 24);
assert.equal(home.querySelector(".p9-button").getAttribute("href"), "browse.html");

// Docs: rendered from USAGE.md with P9 code blocks and tables.
const docsPage = docs.get("docs.html");
assert.ok(docsPage.querySelectorAll(".p9-section > h2").length >= 6);
assert.ok(docsPage.querySelectorAll(".p9-code > pre[tabindex] + button").length >= 6);
for (const table of docsPage.querySelectorAll("table")) {
  assert.ok(table.classList.contains("p9-table") && table.parentElement.matches(".p9-table-scroll[tabindex]"));
}

// Browser: every icon in the data, no id that a #name deep link could hit.
const browse = docs.get("browse.html");
const data = JSON.parse(browse.getElementById("ui-catalog").textContent);
assert.equal(data.length, catalog.length);
for (const icon of catalog) {
  assert.equal(browse.getElementById(icon.name), null, `browse.html: id collides with icon ${icon.name}`);
  for (const style of icon.styles) assert.ok(existsSync(`${site}/svg/${style}/${icon.name}.svg`), `missing svg/${style}/${icon.name}.svg`);
}

// Site CSS stays inside the design system's tokens.
const css = readFileSync("website/site.css", "utf8").replace(/\/\*[\s\S]*?\*\//g, "");
assert.doesNotMatch(css, /#[0-9a-f]{3,8}\b|rgba?\(|hsla?\(|oklch\(/i, "site.css: literal color");
assert.doesNotMatch(css, /box-shadow|text-shadow|gradient|font-family|font-weight|border-radius:\s*\d/i, "site.css: off-token style");
for (const [, property] of css.matchAll(/var\((--[\w-]+)/g)) assert.match(property, /^--p9-/, `site.css: ${property}`);

console.log(`Site verified: ${pages.length} pages, ${links} local links, ${catalog.length} icons with artwork.`);
