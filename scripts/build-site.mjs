// Build https://hugocxl.github.io/stack/ into _site/: the stack home page from website/,
// and one section per library, each built by the package's own site build.
//
//   _site/index.html        website/index.html
//   _site/design-system/    the design-system reference page, as its old Pages site served it
//   _site/icons/            icons/_site      (pnpm run build:site in icons/)
//   _site/vectors/          vectors/_site    (pnpm run build:site in vectors/)
//   _site/sounds/           sounds/_site     (pnpm run build:site in sounds/, reads SITE_VERSION)
//
// Usage: SITE_VERSION=<sounds version> node scripts/build-site.mjs
import { execFileSync } from "node:child_process";
import { cpSync, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const out = join(root, "_site");
const read = (path) => readFileSync(join(root, path), "utf8");
const notJunk = (path) => !path.endsWith(".DS_Store");

// ─── Sections built by their packages ───────────────────────────────────
const built = ["icons", "vectors", "sounds"];
for (const name of built) {
  console.log(`\n▸ ${name}: pnpm run build:site`);
  execFileSync("pnpm", ["run", "build:site"], { cwd: join(root, name), stdio: "inherit", env: process.env });
}

rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });
for (const name of built) cpSync(join(root, name, "_site"), join(out, name), { recursive: true, filter: notJunk });

// The design system served its repository root: the reference page, its assets, DESIGN.md,
// the system/ folder it documents and the published entry points.
const designSystem = ["index.html", "preview.css", "preview.js", "DESIGN.md", "LICENSE", "system", "dist", "skills"];
for (const path of designSystem) {
  const source = join(root, "design-system", path);
  if (!existsSync(source)) throw new Error(`design-system/${path} is missing`);
  cpSync(source, join(out, "design-system", path), { recursive: true, filter: notJunk });
}

// ─── Stack home page ────────────────────────────────────────────────────
// Artwork comes from this repository's own sources, written as DESIGN.md writes it.
const inner = (svg) => svg.trim().replace(/^<svg[^>]*>/, "").replace(/<\/svg>$/, "").split("\n").map((line) => line.trim()).join("");
const icon = (name) =>
  `<svg class="ds-icon" data-icon="${name}" viewBox="0 0 16 16" fill="none" aria-hidden="true">${inner(read(`icons/icons/styles/stroke/${name}.svg`))}</svg>`;
const vector = (name) =>
  read(`vectors/figures/${name}.svg`)
    .trim()
    .replace(' xmlns="http://www.w3.org/2000/svg"', ` class="ds-vector" data-vector="${name}"`)
    .replace(/ color="[^"]*"/, "");

const home = read("website/index.html").replace(/\{\{(icon|vector) ([\w-]+)\}\}/g, (_, kind, name) =>
  kind === "icon" ? icon(name) : vector(name),
);
const unknown = home.match(/\{\{[^}]*\}\}/);
if (unknown) throw new Error(`website/index.html: unknown template value ${unknown[0]}`);
writeFileSync(join(out, "index.html"), home);
cpSync(join(root, "website/site.css"), join(out, "site.css"));
writeFileSync(join(out, ".nojekyll"), "");

console.log(`\nBuilt _site for hugocxl.github.io/stack/ with ${["design-system", ...built].join(", ")} and the home page.`);
