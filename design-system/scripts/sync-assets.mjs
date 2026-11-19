// Refreshes every inline icon and vector on the reference page from the @hugocxl/icons and
// @hugocxl/vectors packages, so the examples always show the published artwork.
// Usage: node scripts/sync-assets.mjs [--check]
import { readFileSync, writeFileSync } from 'node:fs';

const page = new URL('../index.html', import.meta.url);
const html = readFileSync(page, 'utf8');
const svgOf = async specifier => Object.values(await import(specifier))[0];
const inner = svg => svg.replace(/^[\s\S]*?<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '').replace(/\s*\n\s*/g, '').trim();

const icons = new Map();
for (const [, name] of html.matchAll(/<svg class="ds-icon" data-icon="([a-z0-9-]+)"/g)) {
  icons.set(name, inner(await svgOf(`@hugocxl/icons/js/stroke/${name}`)));
}
const vectors = new Map();
for (const [, name] of html.matchAll(/<svg class="ds-vector" data-vector="([a-z0-9-]+)"/g)) {
  const svg = (await svgOf(`@hugocxl/vectors/js/${name}`)).trim();
  vectors.set(name, inner(svg));
}

const synced = html
  .replace(/(<svg class="ds-icon" data-icon="([a-z0-9-]+)"[^>]*>)[\s\S]*?<\/svg>/g, (_, open, name) => open + icons.get(name) + '</svg>')
  .replace(/(<svg class="ds-vector" data-vector="([a-z0-9-]+)"[^>]*>)[\s\S]*?<\/svg>/g, (_, open, name) => open + vectors.get(name) + '</svg>');

const summary = `${icons.size} icons and ${vectors.size} vectors`;
if (process.argv.includes('--check')) {
  if (synced !== html) {
    console.error(`index.html artwork differs from the published packages. Run pnpm run sync.`);
    process.exit(1);
  }
  console.log(`index.html matches @hugocxl/icons and @hugocxl/vectors (${summary}).`);
} else {
  writeFileSync(page, synced);
  console.log(`Synced ${summary} into index.html.`);
}
