// Check the combined site in _site/ as it is served at https://hugocxl.github.io/stack/.
//
// 1. Each package's own site check, run against its section of _site/.
// 2. Every local link, anchor and asset on every page resolves inside _site/, including
//    absolute links to https://hugocxl.github.io/stack/… and the links between sections.
// 3. Every page has the same stack navigation in its masthead, with its own section current.
// 4. No page links to the old per-library sites or repositories, which no longer exist.
//
// Usage: node scripts/check-site.mjs (after scripts/build-site.mjs)
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { existsSync, readdirSync, readFileSync, renameSync, rmSync, statSync, symlinkSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const site = join(root, "_site");
const base = "https://hugocxl.github.io/stack/";
assert.ok(existsSync(join(site, "index.html")), "_site/index.html is missing: run pnpm build:site first");

// jsdom is a dev dependency of icons and vectors; the root has none of its own.
const { JSDOM } = createRequire(join(root, "icons/package.json"))("jsdom");

// ─── 1. Package checks on their sections ────────────────────────────────
// They read <package>/_site, so for the run that path is a link to the section in _site/.
const checks = { icons: ["scripts/check-site.mjs", "--test tests/gallery.test.mjs"], vectors: ["scripts/check-site.mjs"] };
for (const [name, scripts] of Object.entries(checks)) {
  const own = join(root, name, "_site");
  const aside = join(root, name, "_site.own");
  rmSync(aside, { recursive: true, force: true });
  if (existsSync(own)) renameSync(own, aside);
  symlinkSync(join(site, name), own, "dir");
  try {
    for (const script of scripts) {
      console.log(`▸ ${name}: node ${script}`);
      execFileSync(process.execPath, script.split(" "), { cwd: join(root, name), stdio: "inherit" });
    }
  } finally {
    rmSync(own, { force: true });
    if (existsSync(aside)) renameSync(aside, own);
  }
}

// ─── 2. Links, anchors and assets ───────────────────────────────────────
const files = readdirSync(site, { recursive: true }).map(String).filter((path) => statSync(join(site, path)).isFile());
const served = new Set(files);
const pages = files.filter((path) => path.endsWith(".html"));
const documents = new Map();
const documentOf = (path) => {
  if (!documents.has(path)) documents.set(path, new JSDOM(readFileSync(join(site, path), "utf8")).window.document);
  return documents.get(path);
};

// The served file for a URL inside the site, or null for a URL outside it.
function target(url) {
  if (!url.href.startsWith(base)) return null;
  let path = decodeURIComponent(url.pathname.slice(new URL(base).pathname.length));
  if (path === "" || path.endsWith("/")) path += "index.html";
  return path;
}

// Example markup in the design-system reference (specimens and the example page) links to an
// imaginary product's /docs, /download and so on; it is content, not navigation.
const example = ".doc-specimen, .doc-example, pre, code";
const missing = [];
let links = 0;
let assets = 0;
for (const page of pages) {
  const doc = documentOf(page);
  const pageUrl = new URL(page.replace(/(^|\/)index\.html$/, "$1"), base);
  const refs = [
    ...[...doc.querySelectorAll("a[href]")].map((element) => ({ element, value: element.getAttribute("href"), kind: "link" })),
    ...[...doc.querySelectorAll("[src], link[href]")].map((element) => ({
      element,
      value: element.getAttribute("src") ?? element.getAttribute("href"),
      kind: "asset",
    })),
  ];
  for (const { element, value, kind } of refs) {
    if (/^(mailto:|data:|javascript:)/.test(value) || element.closest(example)) continue;
    const url = new URL(value, pageUrl);
    if (!/^https?:$/.test(url.protocol)) continue;
    const path = target(url);
    if (path === null) {
      if (!/^https?:/.test(value)) missing.push(`${page}: ${value} leaves hugocxl.github.io/stack/`);
      continue;
    }
    kind === "link" ? links++ : assets++;
    if (!served.has(path)) {
      missing.push(`${page}: missing ${value} (${path})`);
      continue;
    }
    const hash = decodeURIComponent(url.hash.slice(1));
    if (kind === "link" && hash && path.endsWith(".html") && !documentOf(path).getElementById(hash)) {
      // The icons browser opens #<icon-name> from its own data, not from an element id.
      if (path !== "icons/browse.html") missing.push(`${page}: missing anchor ${value}`);
    }
  }
}
assert.deepEqual(missing, [], `Broken links and assets:\n${missing.join("\n")}`);

// ─── 3. Stack navigation ────────────────────────────────────────────────
const sections = [["Stack", ""], ["Design system", "design-system/"], ["Icons", "icons/"], ["Vectors", "vectors/"], ["Sounds", "sounds/"]];
const redirect = (doc) => doc.querySelector('meta[http-equiv="refresh"]');
let navigated = 0;
for (const page of pages) {
  const doc = documentOf(page);
  // The components website is a preview: its own navigation lists Components, which the other
  // sections add when they move onto the components.
  if (redirect(doc) || page.startsWith("design-system/system/") || page.startsWith("components/")) continue;
  const section = page.includes("/") ? page.split("/")[0] + "/" : "";
  const nav = doc.querySelector("body > .ds-masthead > nav.site-stack:first-child");
  assert.ok(nav, `${page}: no stack navigation first in the masthead`);
  const pageUrl = new URL(page, base);
  const entries = [...nav.querySelectorAll("a")].map((a) => [a.textContent.trim(), target(new URL(a.getAttribute("href"), pageUrl))]);
  assert.deepEqual(entries, sections.map(([label, path]) => [label, `${path}index.html`]), `${page}: stack navigation`);
  assert.deepEqual(
    [...nav.querySelectorAll("[aria-current]")].map((a) => a.textContent.trim()),
    [sections.find(([, path]) => path === section)[0]],
    `${page}: current section`,
  );
  navigated++;
}

// ─── 4. No old addresses ────────────────────────────────────────────────
const old = /hugocxl\.github\.io\/(design-system|icons|vectors|sounds)\b|github(usercontent)?\.com\/hugocxl\/(design-system|icons|vectors|sounds)\b/;
// icons, vectors and sounds copy system/ verbatim from the published @hugocxl/design-system,
// so their copies change with its next release; design-system/system/ is checked here.
const published = (path) => /^(icons|vectors|sounds)\/system\//.test(path);
const stale = [];
for (const path of files.filter((path) => /\.(html|js|css|json|md|txt|svg)$/.test(path) && !published(path))) {
  const text = readFileSync(join(site, path), "utf8");
  const match = text.match(old);
  if (match) stale.push(`${path}: ${match[0]}`);
}
assert.deepEqual(stale, [], `Old site or repository addresses:\n${stale.join("\n")}`);

console.log(
  `Stack site verified: ${pages.length} pages, ${links} local links and ${assets} assets resolve, ${navigated} pages with the stack navigation, no old addresses.`,
);
