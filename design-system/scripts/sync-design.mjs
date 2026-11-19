// Copies each component specimen from index.html into its marked block in DESIGN.md,
// so the Markdown an agent reads is the markup the reference page renders.
// Usage: node scripts/sync-design.mjs [--check]
import { readFileSync, writeFileSync } from 'node:fs';

const root = new URL('../', import.meta.url);
const html = readFileSync(new URL('index.html', root), 'utf8');
const designPath = new URL('DESIGN.md', root);
const design = readFileSync(designPath, 'utf8');

function specimen(id) {
  const open = html.indexOf(`<div class="doc-specimen" data-component="${id}">`);
  if (open < 0) throw new Error(`index.html has no specimen for "${id}"`);
  const start = html.indexOf('>', open) + 1;
  const tags = /<\/?div\b/g;
  tags.lastIndex = start;
  let depth = 1;
  let match;
  while ((match = tags.exec(html)) && (depth += match[0] === '<div' ? 1 : -1) > 0);
  const lines = html.slice(start, match.index).replace(/^\n+|\s+$/g, '').split('\n');
  const indent = Math.min(...lines.filter(line => line.trim()).map(line => line.match(/^ */)[0].length));
  return elide(lines.map(line => line.slice(indent)).join('\n'));
}

// Icon and vector paths come from their packages; the markup keeps the element and its title.
function elide(markup) {
  return markup.replace(/(<svg class="ds-(vector|icon)"[^>]*>)([\s\S]*?)<\/svg>/g, (_, open, kind, inner) =>
    open + (kind === 'vector' ? (inner.match(/<title>[\s\S]*?<\/title>/) || [''])[0] : '') + `<!-- paths from @hugocxl/${kind}s -->` + '</svg>');
}

const ids = [...html.matchAll(/class="doc-specimen" data-component="([a-z-]+)"/g)].map(m => m[1]);
const marked = [...design.matchAll(/<!-- specimen:([a-z-]+) -->/g)].map(m => m[1]);
if (ids.join() !== marked.join()) {
  console.error(`Specimens in index.html (${ids}) and DESIGN.md (${marked}) differ.`);
  process.exit(1);
}

const synced = design.replace(
  /<!-- specimen:([a-z-]+) -->[\s\S]*?<!-- \/specimen -->/g,
  (_, id) => `<!-- specimen:${id} -->\n\`\`\`html\n${specimen(id)}\n\`\`\`\n<!-- /specimen -->`,
);

if (process.argv.includes('--check')) {
  if (synced !== design) {
    console.error('DESIGN.md component markup is out of date. Run npm run sync.');
    process.exit(1);
  }
  console.log(`DESIGN.md matches ${ids.length} specimens.`);
} else {
  writeFileSync(designPath, synced);
  console.log(`Synced ${ids.length} specimens into DESIGN.md.`);
}
