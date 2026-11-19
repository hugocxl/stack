#!/usr/bin/env node
// Search the @hugocxl/icons catalog, or check that icon names exist.
//
//   node search.mjs <words…> [--style duotone|solid|stroke] [--limit 12] [--json]
//   node search.mjs --check <name…>
//
// Reads the catalog of the project's installed @hugocxl/icons first, so results match the
// version in use, and falls back to the catalog shipped with this package.
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

// Words people search for that the catalog spells differently.
export const SYNONYMS = {
  add: ['plus'],
  alert: ['triangle-alert', 'bell'],
  bin: ['trash'],
  cancel: ['close'],
  cog: ['settings'],
  cross: ['close'],
  delete: ['trash'],
  done: ['check', 'circle-check'],
  edit: ['pencil'],
  error: ['circle-x'],
  gear: ['settings'],
  hamburger: ['menu'],
  house: ['home'],
  info: ['circle-info'],
  notification: ['bell'],
  options: ['ellipsis', 'settings'],
  preferences: ['settings'],
  profile: ['user'],
  remove: ['trash', 'minus', 'close'],
  success: ['circle-check'],
  times: ['close'],
  warning: ['triangle-alert'],
  x: ['close'],
};

export function loadCatalog(cwd = process.cwd()) {
  const candidates = [];
  try {
    candidates.push(createRequire(join(cwd, 'package.json')).resolve('@hugocxl/icons/catalog.json'));
  } catch {}
  candidates.push(fileURLToPath(new URL('../../../dist/catalog.json', import.meta.url)));
  for (const file of candidates) {
    try {
      return JSON.parse(readFileSync(file, 'utf8'));
    } catch {}
  }
  throw new Error('Cannot find @hugocxl/icons/catalog.json. Install @hugocxl/icons in this project.');
}

export const exportName = name => name.split('-').map(part => part[0].toUpperCase() + part.slice(1)).join('') + 'Icon';

const words = text => text.toLowerCase().split(/[^a-z0-9]+/).filter(Boolean);

export function search(catalog, query, { style, limit = 12 } = {}) {
  const terms = words(query);
  const aliases = new Set(terms.flatMap(term => SYNONYMS[term] ?? []));
  const phrase = terms.join('-');
  const scored = [];
  for (const icon of catalog) {
    if (style && !icon.styles.includes(style)) continue;
    const parts = icon.name.split('-');
    const tags = icon.tags.flatMap(words);
    const category = words(icon.category);
    let score = icon.name === phrase ? 100 : aliases.has(icon.name) ? 60 : 0;
    let matched = 0;
    for (const term of terms) {
      const termScore = parts.includes(term) ? 30
        : tags.includes(term) ? 18
        : icon.name.includes(term) ? 12
        : tags.some(tag => tag.startsWith(term)) ? 8
        : category.includes(term) ? 4
        : 0;
      if (termScore) matched++;
      score += termScore;
    }
    if (terms.length > 1 && matched === terms.length) score += 20;
    if (score > 0) scored.push({ icon, score });
  }
  scored.sort((a, b) => b.score - a.score || a.icon.name.length - b.icon.name.length || a.icon.name.localeCompare(b.icon.name));
  return scored.slice(0, limit).map(({ icon }) => icon);
}

function distance(a, b) {
  let row = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    const next = [i];
    for (let j = 1; j <= b.length; j++) next[j] = Math.min(row[j] + 1, next[j - 1] + 1, row[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    row = next;
  }
  return row[b.length];
}

export function suggest(catalog, name, limit = 3) {
  const close = catalog.map(icon => ({ name: icon.name, d: distance(name, icon.name) }))
    .filter(({ d }) => d <= (name.length <= 3 ? 1 : Math.max(2, Math.floor(name.length / 4))))
    .sort((a, b) => a.d - b.d || a.name.localeCompare(b.name)).map(({ name }) => name);
  const related = search(catalog, name.replace(/-/g, ' '), { limit }).map(icon => icon.name);
  return [...new Set([...(SYNONYMS[name] ?? []), ...close, ...related])].slice(0, limit);
}

export function check(catalog, names) {
  const known = new Set(catalog.map(icon => icon.name));
  return names.filter(name => !known.has(name)).map(name => ({ name, suggestions: suggest(catalog, name) }));
}

function describe(icon) {
  const color = icon.defaultColor ? `  color: ${icon.defaultColor}` : '';
  return `${icon.name.padEnd(28)} ${exportName(icon.name).padEnd(32)} ${icon.styles.join('/').padEnd(20)} ${icon.category}${color}`;
}

function main(argv) {
  const options = { limit: 12 };
  const rest = [];
  let mode = 'search';
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--json') options.json = true;
    else if (arg === '--check') mode = 'check';
    else if (arg === '--style') options.style = argv[++i];
    else if (arg === '--limit') options.limit = Number(argv[++i]);
    else if (arg === '--help' || arg === '-h') mode = 'help';
    else rest.push(arg);
  }
  if (mode === 'help' || rest.length === 0) {
    console.log('Usage: search.mjs <words…> [--style duotone|solid|stroke] [--limit n] [--json]\n       search.mjs --check <name…>');
    return mode === 'help' ? 0 : 1;
  }
  const catalog = loadCatalog();
  if (mode === 'check') {
    const missing = check(catalog, rest);
    if (options.json) console.log(JSON.stringify({ missing }, null, 2));
    else if (missing.length === 0) console.log(`All ${rest.length} icon names exist.`);
    else for (const { name, suggestions } of missing) console.log(`Unknown icon "${name}". Did you mean: ${suggestions.join(', ') || 'no close match'}?`);
    return missing.length ? 1 : 0;
  }
  const results = search(catalog, rest.join(' '), options);
  if (options.json) console.log(JSON.stringify(results.map(icon => ({ ...icon, export: exportName(icon.name) })), null, 2));
  else if (results.length === 0) console.log('No icons match. Try a broader word, or browse https://hugocxl.github.io/stack/icons/browse.html');
  else console.log(results.map(describe).join('\n'));
  return results.length ? 0 : 1;
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  process.exitCode = main(process.argv.slice(2));
}
