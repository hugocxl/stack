// Build the GitHub Pages site from website/ into _site/.
// Pages follow the design system from the @hugocxl/design-system package; the sounds come from this repository.
import { cpSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, join } from "node:path";
import { build } from "esbuild";
import { marked } from "marked";
import { sounds, soundNames, groups, feedback } from "../packages/sounds/dist/index.js";

const out = "_site";
const require = createRequire(import.meta.url);
const designSystem = dirname(require.resolve("@hugocxl/design-system/package.json"));
const read = (path) => readFileSync(path, "utf8");
const escape = (text) =>
  String(text).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);

const version = process.env.SITE_VERSION || JSON.parse(read("packages/sounds/package.json")).version;
const facts = { count: String(soundNames.length), haptics: String(Object.keys(feedback).length), version };

// ─── Artwork from the stack ─────────────────────────────────────────────
const loadIcon = async (name) => Object.values(await import(`@hugocxl/icons/js/stroke/${name}`))[0];
const loadVector = async (name) => Object.values(await import(`@hugocxl/vectors/js/${name}`))[0];
const icon = async (name) =>
  (await loadIcon(name))
    .trim()
    .replace(/<svg [^>]*>/, `<svg class="ds-icon" data-icon="${name}" viewBox="0 0 16 16" fill="none" aria-hidden="true">`);
const vector = async (name) =>
  (await loadVector(name))
    .trim()
    .replace(' xmlns="http://www.w3.org/2000/svg"', ` class="ds-vector" data-vector="${name}"`)
    .replace(/ color="[^"]*"/, "");

// ─── Listen: one section per group ──────────────────────────────────────
const hz = (value) => `${value} Hz`;
const layers = (sound) =>
  sound.layers
    .map((l) => (l.kind === "noise" ? `${l.filter ?? "bandpass"} noise ${hz(l.freq)}` : `${l.wave ?? "sine"} ${l.to ? `${l.freq} to ${hz(l.to)}` : hz(l.freq)}`))
    .join(" + ");
const play = await icon("play-triangle");
const download = await icon("download");
let number = 0;
const soundSections = Object.entries(groups)
  .map(([group, heading]) => {
    const rows = soundNames
      .filter((name) => sounds[name].group === group)
      .map((name) => {
        number += 1;
        return `          <li>
            <span class="ds-label">${String(number).padStart(2, "0")}</span>
            <div>
              <button class="site-play" type="button" data-sound="${name}">${play}${name}</button>
              <p>${escape(sounds[name].description)} <span class="ds-label site-layers">${escape(layers(sounds[name]))}</span></p>
            </div>
            <button class="site-text-button" type="button" data-wav="${name}" aria-label="Download ${name} as WAV">${download}WAV</button>
          </li>`;
      })
      .join("\n");
    return `      <section class="ds-section" id="${group}">
        <h2>${heading}</h2>
        <ol class="site-sounds">
${rows}
        </ol>
      </section>`;
  })
  .join("\n");
const hapticButtons = Object.entries(feedback)
  .map(([kind, { sound }]) => `          <button class="site-text-button" type="button" data-haptic="${kind}" aria-label="${kind}, plays ${sound}">${kind}</button>`)
  .join("\n");

// ─── Docs: docs/USAGE.md rendered into sections ─────────────────────────
const slug = (text) => text.toLowerCase().replace(/[^\w\s-]/g, "").replace(/\s/g, "-");
const github = "https://github.com/hugocxl/sounds/blob/main/";
const renderer = new marked.Renderer();
renderer.code = ({ text }) =>
  `<div class="ds-code"><pre tabindex="0"><code>${escape(text)}</code></pre><button type="button">Copy</button></div>\n`;
const baseTable = renderer.table.bind(renderer);
renderer.table = (token) =>
  `<div class="ds-table-scroll" tabindex="0">${baseTable(token).replace("<table>", '<table class="ds-table">')}</div>\n`;
renderer.link = function ({ href, title, tokens }) {
  const target = href.replace(/^\.\.\/(.+)$/, `${github}$1`);
  return `<a href="${escape(target)}"${title ? ` title="${escape(title)}"` : ""}>${this.parser.parseInline(tokens)}</a>`;
};

const tokens = marked.lexer(read("docs/USAGE.md"));
let docsTitle = "Docs";
const docGroups = [{ id: null, heading: null, tokens: [] }];
for (const token of tokens) {
  if (token.type === "heading" && token.depth === 1) docsTitle = token.text;
  else if (token.type === "heading" && token.depth === 2) docGroups.push({ id: slug(token.text), heading: token, tokens: [] });
  else docGroups.at(-1).tokens.push(token);
}
const docs = docGroups
  .filter((group) => group.heading || group.tokens.some((token) => token.type !== "space"))
  .map((group) => {
    const body = marked.parser(Object.assign(group.tokens, { links: tokens.links }), { renderer });
    const heading = group.heading ? `<h2>${marked.parseInline(group.heading.text)}</h2>\n` : "";
    return `      <section class="ds-section"${group.id ? ` id="${group.id}"` : ""}>\n${heading}${body}      </section>`;
  })
  .join("\n");

// ─── Templates ──────────────────────────────────────────────────────────
const partial = (name) => read(`website/partials/${name}.html`).replace(/\n$/, "");
async function render(template, values) {
  let html = template
    .replace(/\{\{([\w-]+)\}\}/g, (match, key) => (key in values ? values[key] : match))
    .replace(/\{\{head ([^}]*)\}\}/, (_, args) => {
      const attributes = Object.fromEntries([...args.matchAll(/(\w+)="([^"]*)"/g)].map((m) => [m[1], m[2]]));
      return partial("head").replace(/\{\{(\w+)\}\}/g, (__, key) => attributes[key] ?? "");
    })
    .replace("{{masthead}}", partial("masthead"))
    .replace("{{footer}}", partial("footer"));
  for (const [match, kind, name] of html.matchAll(/\{\{(icon|vector) ([\w-]+)\}\}/g)) {
    html = html.replace(match, kind === "icon" ? await icon(name) : await vector(name));
  }
  const unknown = html.match(/\{\{[^}]*\}\}/);
  if (unknown) throw new Error(`Unknown template value ${unknown[0]}`);
  return html;
}

rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });
cpSync(join(designSystem, "system"), `${out}/system`, { recursive: true });
cpSync("website/site.css", `${out}/site.css`);
await build({ entryPoints: ["website/site.ts"], bundle: true, format: "esm", minify: true, outfile: `${out}/site.js`, logLevel: "warning" });

const values = { ...facts, sounds: soundSections, "haptic-buttons": hapticButtons, docs, "docs-title": escape(docsTitle) };
for (const page of ["index.html", "listen.html", "docs.html"]) {
  writeFileSync(`${out}/${page}`, await render(read(`website/${page}`), values));
}
writeFileSync(`${out}/.nojekyll`, "");
console.log(`Built site with ${facts.count} sounds and ${facts.haptics} haptics.`);
