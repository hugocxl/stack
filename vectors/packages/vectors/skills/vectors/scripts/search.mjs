#!/usr/bin/env node
// Search the @hugocxl/vectors catalog by meaning, or check that vector names exist.
//
//   node search.mjs <words…> [--category <id>] [--limit 10] [--json]
//   node search.mjs --categories
//   node search.mjs --check <name…>
//
// Reads the catalog of the project's installed @hugocxl/vectors first, so results match the
// version in use, and falls back to the catalog shipped with this package.
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

export function loadCatalog(cwd = process.cwd()) {
  const candidates = [];
  try {
    candidates.push(createRequire(join(cwd, 'package.json')).resolve('@hugocxl/vectors/catalog.json'));
  } catch {}
  candidates.push(fileURLToPath(new URL('../../../dist/catalog.json', import.meta.url)));
  for (const file of candidates) {
    try {
      return JSON.parse(readFileSync(file, 'utf8'));
    } catch {}
  }
  throw new Error('Cannot find @hugocxl/vectors/catalog.json. Install @hugocxl/vectors in this project.');
}

const STOP = new Set(['a', 'an', 'and', 'for', 'in', 'of', 'on', 'the', 'to', 'with', 'page', 'section']);
const words = text => text.toLowerCase().split(/[^a-z0-9]+/).filter(word => word && !STOP.has(word));
// A light stem so "payments" finds "payment" and "onboarding" finds "onboard".
const stem = word => word.replace(/(ings?|ed|es|s)$/, '') || word;

const PRIORITY = { core: 6, extended: 2, specialist: 0 };

export function search(catalog, query, { category, limit = 10 } = {}) {
  const terms = words(query).map(stem);
  const phrase = words(query).join('-');
  const scored = [];
  for (const vector of catalog) {
    if (category && vector.categoryId !== category) continue;
    const fields = [
      [words(vector.name).map(stem), 30],
      [words(vector.title).map(stem), 24],
      [words(vector.placement).map(stem), 14],
      [words(vector.category).map(stem), 8],
      [words(vector.description).map(stem), 6],
    ];
    let score = vector.name === phrase ? 100 : 0;
    let matched = 0;
    for (const term of terms) {
      const best = Math.max(0, ...fields.map(([list, weight]) => (list.includes(term) ? weight : 0)));
      if (best) matched++;
      score += best;
    }
    if (matched === 0) continue;
    if (terms.length > 1 && matched === terms.length) score += 25;
    scored.push({ vector, score: score + PRIORITY[vector.priority] });
  }
  scored.sort((a, b) => b.score - a.score || a.vector.name.localeCompare(b.vector.name));
  return scored.slice(0, limit).map(({ vector }) => vector);
}

export function categories(catalog) {
  const counts = new Map();
  for (const { categoryId, category } of catalog) counts.set(categoryId, { category, count: (counts.get(categoryId)?.count ?? 0) + 1 });
  return [...counts].map(([id, { category, count }]) => ({ id, category, count }));
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
  const close = catalog.map(vector => ({ name: vector.name, d: distance(name, vector.name) }))
    .filter(({ d }) => d <= Math.max(2, Math.floor(name.length / 5)))
    .sort((a, b) => a.d - b.d || a.name.localeCompare(b.name)).map(({ name }) => name);
  const related = search(catalog, name.replace(/-/g, ' '), { limit }).map(vector => vector.name);
  return [...new Set([...close, ...related])].slice(0, limit);
}

export function check(catalog, names) {
  const known = new Set(catalog.map(vector => vector.name));
  return names.filter(name => !known.has(name)).map(name => ({ name, suggestions: suggest(catalog, name) }));
}

function main(argv) {
  const options = { limit: 10 };
  const rest = [];
  let mode = 'search';
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--json') options.json = true;
    else if (arg === '--check') mode = 'check';
    else if (arg === '--categories') mode = 'categories';
    else if (arg === '--category') options.category = argv[++i];
    else if (arg === '--limit') options.limit = Number(argv[++i]);
    else if (arg === '--help' || arg === '-h') mode = 'help';
    else rest.push(arg);
  }
  if (mode === 'help' || (mode !== 'categories' && rest.length === 0)) {
    console.log('Usage: search.mjs <words…> [--category id] [--limit n] [--json]\n       search.mjs --categories\n       search.mjs --check <name…>');
    return mode === 'help' ? 0 : 1;
  }
  const catalog = loadCatalog();
  if (mode === 'categories') {
    const list = categories(catalog);
    console.log(options.json ? JSON.stringify(list, null, 2) : list.map(c => `${c.id.padEnd(44)} ${String(c.count).padStart(4)}  ${c.category}`).join('\n'));
    return 0;
  }
  if (mode === 'check') {
    const missing = check(catalog, rest);
    if (options.json) console.log(JSON.stringify({ missing }, null, 2));
    else if (missing.length === 0) console.log(`All ${rest.length} vector names exist.`);
    else for (const { name, suggestions } of missing) console.log(`Unknown vector "${name}". Did you mean: ${suggestions.join(', ') || 'no close match'}?`);
    return missing.length ? 1 : 0;
  }
  const results = search(catalog, rest.join(' '), options);
  if (options.json) console.log(JSON.stringify(results, null, 2));
  else if (results.length === 0) console.log('No vectors match. Try other words, or browse https://hugocxl.github.io/vectors/browse.html');
  else console.log(results.map(v => `${v.name}  (${v.export})\n  ${v.title} · ${v.placement}\n  ${v.description}`).join('\n\n'));
  return results.length ? 0 : 1;
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  process.exitCode = main(process.argv.slice(2));
}
