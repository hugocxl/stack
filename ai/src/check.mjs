// `npx @hugocxl/ai check`: find the mistakes agents make with the stack, using the catalogs of the
// libraries installed in the project.
import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { extname, join, sep } from 'node:path';
import { pathToFileURL } from 'node:url';
import { libraries, readManifest, settings } from './project.mjs';
import { plan } from './sync.mjs';

export const RULES = {
  'agent-files': { level: 'error', summary: 'AGENTS.md and the skills match the installed libraries' },
  'no-claude-md': { level: 'error', summary: 'no CLAUDE.md files; use AGENTS.md only' },
  'agents-md-size': { level: 'warning', summary: 'AGENTS.md stays concise (under 200 lines)' },
  'foreign-icons': { level: 'error', summary: 'no icon library other than @hugocxl/icons' },
  'unknown-icon': { level: 'error', summary: 'every @hugocxl/icons import, export and name exists' },
  'unknown-vector': { level: 'error', summary: 'every @hugocxl/vectors import, export and name exists' },
  'unknown-sound': { level: 'error', summary: 'every sound and haptic passed to @hugocxl/sounds exists' },
  'missing-library': { level: 'error', summary: 'every imported @hugocxl library is installed' },
  'tailwind-palette': { level: 'warning', summary: "no Tailwind default palette next to the design system's tokens" },
  'raw-color': { level: 'warning', summary: 'no raw color values in stylesheets next to the design system' },
};

export const FOREIGN_ICON_PACKAGES = [
  /^lucide(-[a-z]+)*$/, /^@lucide\//, /^react-icons(\/|$)/, /^@heroicons\//, /^heroicons$/, /^@phosphor-icons\//, /^phosphor-react$/,
  /^@tabler\/icons/, /^@fortawesome\//, /^@mui\/icons-material/, /^@radix-ui\/react-icons$/, /^@iconify(-json)?\//, /^@iconify\/react$/,
  /^react-feather$/, /^feather-icons$/, /^@ant-design\/icons/, /^ionicons$/, /^@expo\/vector-icons/, /^react-native-vector-icons/,
  /^bootstrap-icons$/, /^react-bootstrap-icons$/, /^remixicon$/, /^@remixicon\//, /^@primer\/octicons/, /^@carbon\/icons/, /^@mdi\//,
  /^unplugin-icons/, /^@hugeicons\//, /^iconoir(-react)?$/, /^@iconscout\//, /^react-ionicons$/, /^@svgr\/.*icons/,
];

const CODE = new Set(['.js', '.jsx', '.mjs', '.cjs', '.ts', '.tsx', '.mts', '.cts', '.vue', '.svelte', '.astro', '.html', '.htm', '.md', '.mdx']);
const STYLES = new Set(['.css', '.scss', '.sass', '.less', '.pcss']);
const SKIP_DIRS = new Set(['node_modules', '.git', 'dist', 'build', 'out', '.next', '.nuxt', '.svelte-kit', '.astro', '.output', '.vercel',
  '.turbo', '.cache', 'coverage', 'vendor', '.agents', '.claude', 'Pods', 'DerivedData', '.expo']);
const SKIP_FILES = new Set(['AGENTS.md', 'CLAUDE.md', 'CHANGELOG.md']);

/** Turn a glob such as `legacy/**` or `*.test.tsx` into a RegExp over relative paths. */
export function globToRegExp(glob) {
  let pattern = '';
  for (let i = 0; i < glob.length; i++) {
    const c = glob[i];
    if (c === '*' && glob[i + 1] === '*') { pattern += '.*'; i++; if (glob[i + 1] === '/') i++; }
    else if (c === '*') pattern += '[^/]*';
    else if (c === '?') pattern += '[^/]';
    else pattern += c.replace(/[.+^${}()|[\]\\]/g, '\\$&');
  }
  return new RegExp(`^${pattern}(/.*)?$`);
}

/** Source files to check: git's tracked and untracked files when possible, otherwise a walk. */
export function sourceFiles(root, ignore = []) {
  const ignored = ignore.map(globToRegExp);
  let files;
  try {
    files = execFileSync('git', ['ls-files', '-co', '--exclude-standard'], { cwd: root, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'], maxBuffer: 1 << 28 })
      .split('\n').filter(Boolean);
  } catch {
    files = [];
    const walk = dir => {
      for (const entry of readdirSync(join(root, dir), { withFileTypes: true })) {
        const path = dir ? `${dir}/${entry.name}` : entry.name;
        if (entry.isDirectory()) { if (!SKIP_DIRS.has(entry.name)) walk(path); }
        else files.push(path);
      }
    };
    walk('');
  }
  return files.filter(file => {
    const parts = file.split('/');
    if (parts.some(part => SKIP_DIRS.has(part)) || SKIP_FILES.has(parts.at(-1))) return false;
    if (ignored.some(re => re.test(file))) return false;
    const ext = extname(file).toLowerCase();
    return (CODE.has(ext) || STYLES.has(ext)) && existsSync(join(root, file)) && statSync(join(root, file)).size < 2_000_000;
  });
}

const exportName = (name, suffix) => name.split('-').map(part => part[0].toUpperCase() + part.slice(1)).join('') + suffix;

function lineAt(text, index) {
  let line = 1;
  let last = -1;
  for (let i = text.indexOf('\n'); i !== -1 && i < index; i = text.indexOf('\n', i + 1)) { line++; last = i; }
  return { line, column: index - last };
}

/** `import`, `export … from`, `require()` and `import()` specifiers, with any named bindings. */
export function importsOf(text) {
  const found = [];
  const named = /\b(?:import|export)\s+(?:type\s+)?(?:([\w$]+)\s*,?\s*)?(?:\{([^}]*)\}|\*\s+as\s+[\w$]+)?\s*from\s*['"]([^'"]+)['"]/g;
  for (const m of text.matchAll(named)) {
    const names = (m[2] ?? '').split(',').map(part => part.trim().replace(/^type\s+/, '').split(/\s+as\s+/)[0].trim()).filter(Boolean);
    found.push({ specifier: m[3], names, index: m.index });
  }
  for (const m of text.matchAll(/\b(?:require|import)\s*\(\s*['"]([^'"]+)['"]\s*\)/g)) found.push({ specifier: m[1], names: [], index: m.index });
  for (const m of text.matchAll(/^\s*import\s+['"]([^'"]+)['"]/gm)) found.push({ specifier: m[1], names: [], index: m.index });
  for (const m of text.matchAll(/@import\s+(?:url\()?['"]([^'"]+)['"]/g)) found.push({ specifier: m[1], names: [], index: m.index });
  return found;
}

async function loadKnowledge(root, libs) {
  const by = Object.fromEntries(libs.map(library => [library.id, library]));
  const knowledge = { installed: new Set(libs.filter(l => l.installed).map(l => l.package)) };
  if (by.icons.installed) {
    const catalog = JSON.parse(readFileSync(join(by.icons.dir, 'dist/catalog.json'), 'utf8'));
    knowledge.icons = new Map(catalog.map(icon => [icon.name, icon]));
    knowledge.iconExports = new Map(catalog.map(icon => [exportName(icon.name, 'Icon'), icon]));
  }
  if (by.vectors.installed) {
    const catalog = JSON.parse(readFileSync(join(by.vectors.dir, 'dist/catalog.json'), 'utf8'));
    knowledge.vectors = new Map(catalog.map(vector => [vector.name, vector]));
    knowledge.vectorExports = new Set(catalog.map(vector => vector.export));
  }
  if (by.sounds.installed) {
    const sounds = await import(pathToFileURL(join(by.sounds.dir, 'dist/index.js')).href);
    knowledge.sounds = new Set(sounds.soundNames);
    knowledge.haptics = new Set(Object.keys(sounds.feedback));
  }
  knowledge.designSystem = by['design-system'].installed;
  return knowledge;
}

const ICON_PATH = /^@hugocxl\/icons(?:\/(js|react|react-native)(?:\/(duotone|solid|stroke))?(?:\/([a-z0-9-]+))?)?$/;
const VECTOR_PATH = /^@hugocxl\/vectors(?:\/(js|react|react-native)(?:\/([a-z0-9-]+))?)?$/;

function checkIconImport({ specifier, names }, k, report) {
  if (['@hugocxl/icons/catalog.json', '@hugocxl/icons/colors', '@hugocxl/icons/package.json'].includes(specifier)) return;
  const m = specifier.match(ICON_PATH);
  if (!m) return report('unknown-icon', `"${specifier}" is not an @hugocxl/icons export. Use /js, /react or /react-native, an optional /stroke, /solid or /duotone, and an optional icon name.`);
  let [, , style, name] = m;
  if (name && ['duotone', 'solid', 'stroke'].includes(name) && !style) { style = name; name = undefined; }
  if (name) {
    const icon = k.icons.get(name);
    if (!icon) return report('unknown-icon', `There is no icon named "${name}". Find one with the icons skill's search script.`);
    if (style && !icon.styles.includes(style)) return report('unknown-icon', `"${name}" has no ${style} style (it has ${icon.styles.join(', ')}).`);
    for (const binding of names) {
      if (binding !== exportName(name, 'Icon')) report('unknown-icon', `"${specifier}" exports ${exportName(name, 'Icon')}, not ${binding}.`);
    }
    return;
  }
  for (const binding of names) {
    const icon = k.iconExports.get(binding);
    if (!icon) report('unknown-icon', `@hugocxl/icons has no export named ${binding}. Find the icon with the icons skill's search script.`);
    else if (style && !icon.styles.includes(style)) report('unknown-icon', `${binding} has no ${style} style (it has ${icon.styles.join(', ')}).`);
  }
}

function checkVectorImport({ specifier, names }, k, report) {
  if (['@hugocxl/vectors/catalog.json', '@hugocxl/vectors/package.json'].includes(specifier)) return;
  const m = specifier.match(VECTOR_PATH);
  if (!m) return report('unknown-vector', `"${specifier}" is not an @hugocxl/vectors export. Use /js, /react or /react-native and an optional vector name.`);
  const [, , name] = m;
  if (name) {
    const vector = k.vectors.get(name);
    if (!vector) return report('unknown-vector', `There is no vector named "${name}". Find one with the vectors skill's search script.`);
    for (const binding of names) if (binding !== vector.export) report('unknown-vector', `"${specifier}" exports ${vector.export}, not ${binding}.`);
    return;
  }
  for (const binding of names) {
    if (!k.vectorExports.has(binding)) report('unknown-vector', `@hugocxl/vectors has no export named ${binding}. Find the vector with the vectors skill's search script.`);
  }
}

const PALETTE = /(?<![\w-])(?:[a-z0-9-]+:)*(?:bg|text|border(?:-[trblxy])?|ring|ring-offset|fill|stroke|from|via|to|outline|divide|placeholder|decoration|accent|caret|shadow)-(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-(?:50|[1-9]00|950)(?:\/\d+)?(?![\w-])|(?<![\w-])(?:[a-z0-9-]+:)*(?:bg|text|border)-(?:white|black)(?![\w-])/g;
const RAW_COLOR = /#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?|oklch|oklab|lab|lch)\(/g;

/** Check one file's text. Returns findings without the file path. */
export function checkText(file, text, k) {
  const findings = [];
  const lines = text.split('\n');
  const report = (rule, message, index) => {
    const { line, column } = lineAt(text, index);
    if (/stack-ignore/.test(lines[line - 1] ?? '') || /stack-ignore-next-line/.test(lines[line - 2] ?? '')) return;
    findings.push({ rule, message, line, column });
  };
  const ext = extname(file).toLowerCase();
  const imports = importsOf(text);

  for (const entry of imports) {
    const at = (rule, message) => report(rule, message, entry.index);
    if (FOREIGN_ICON_PACKAGES.some(re => re.test(entry.specifier))) {
      at('foreign-icons', `"${entry.specifier}" is another icon library. Use @hugocxl/icons; the icons skill shows how.`);
      continue;
    }
    const pkg = entry.specifier.match(/^@hugocxl\/[a-z-]+/)?.[0];
    if (!pkg || pkg === '@hugocxl/ai') continue;
    if (!k.installed.has(pkg)) { at('missing-library', `${pkg} is imported but not installed. Run npm install ${pkg}.`); continue; }
    if (pkg === '@hugocxl/icons') checkIconImport(entry, k, at);
    if (pkg === '@hugocxl/vectors') checkVectorImport(entry, k, at);
  }

  if (k.icons) {
    for (const m of text.matchAll(/data-icon=["']([a-z0-9-]+)["']/g)) {
      if (!k.icons.has(m[1])) report('unknown-icon', `There is no icon named "${m[1]}". Find one with the icons skill's search script.`, m.index);
    }
  }
  if (k.vectors) {
    for (const m of text.matchAll(/data-vector=["']([a-z0-9-]+)["']/g)) {
      if (!k.vectors.has(m[1])) report('unknown-vector', `There is no vector named "${m[1]}". Find one with the vectors skill's search script.`, m.index);
    }
  }
  if (k.sounds && imports.some(entry => entry.specifier === '@hugocxl/sounds')) {
    for (const m of text.matchAll(/\bplay\(\s*['"]([^'"]+)['"]/g)) {
      if (!k.sounds.has(m[1])) report('unknown-sound', `There is no sound named "${m[1]}". The sounds are ${[...k.sounds].join(', ')}.`, m.index);
    }
    for (const m of text.matchAll(/\bhaptic\(\s*['"]([^'"]+)['"]/g)) {
      if (!k.haptics.has(m[1])) report('unknown-sound', `There is no haptic named "${m[1]}". The haptics are ${[...k.haptics].join(', ')}.`, m.index);
    }
  }
  if (k.designSystem) {
    if (CODE.has(ext)) {
      for (const m of text.matchAll(PALETTE)) {
        report('tailwind-palette', `"${m[0]}" uses Tailwind's default palette. Use the design system's token utilities (bg-canvas, text-ink, text-muted, border-rule…).`, m.index);
      }
    }
    if (STYLES.has(ext)) {
      for (const m of text.matchAll(RAW_COLOR)) {
        const { line, column } = lineAt(text, m.index);
        const declaration = lines[line - 1].slice(0, column - 1).split(/[;{]/).pop();
        if (/^\s*--[\w-]+\s*:/.test(declaration)) continue; // defining a custom property is how tokens are made
        report('raw-color', `"${m[0]}" is a raw color. Use a design-system token such as var(--ds-ink) or var(--ds-muted).`, m.index);
      }
    }
  }
  return findings;
}

function checkManifest(root) {
  const manifest = readManifest(root);
  const findings = [];
  for (const field of ['dependencies', 'devDependencies', 'peerDependencies']) {
    for (const name of Object.keys(manifest[field] ?? {})) {
      if (FOREIGN_ICON_PACKAGES.some(re => re.test(name))) {
        findings.push({ file: 'package.json', line: 1, column: 1, rule: 'foreign-icons', message: `${name} is another icon library. Remove it and use @hugocxl/icons.` });
      }
    }
  }
  return findings;
}

function checkAgentFiles(root) {
  const { write, remove } = plan(root);
  const findings = [
    ...write.map(({ path, created }) => ({ file: path, line: 1, column: 1, rule: 'agent-files', message: created ? 'is missing. Run npx @hugocxl/ai sync.' : 'is out of date with the installed libraries. Run npx @hugocxl/ai sync.' })),
    ...remove.map(({ path }) => ({ file: path, line: 1, column: 1, rule: 'agent-files', message: 'belongs to a library or version that is no longer installed. Run npx @hugocxl/ai sync.' })),
  ];
  if (existsSync(join(root, 'CLAUDE.md'))) {
    findings.push({ file: 'CLAUDE.md', line: 1, column: 1, rule: 'no-claude-md', message: 'Remove CLAUDE.md and keep project instructions in AGENTS.md only.' });
  }
  const agentsPath = join(root, 'AGENTS.md');
  if (existsSync(agentsPath)) {
    const lineCount = readFileSync(agentsPath, 'utf8').split('\n').length;
    if (lineCount > 200) {
      findings.push({ file: 'AGENTS.md', line: 1, column: 1, rule: 'agents-md-size', message: `AGENTS.md has ${lineCount} lines; keep it under 200 lines (WHY-only).` });
    }
  }
  return findings;
}

/** Run every rule over the project. Findings carry their level after the project's settings. */
export async function check(root, { files } = {}) {
  const config = settings(root);
  const levels = Object.fromEntries(Object.entries(RULES).map(([rule, { level }]) => [rule, config.rules[rule] ?? level]));
  const knowledge = await loadKnowledge(root, libraries(root));
  const findings = [...checkAgentFiles(root), ...checkManifest(root)];
  const list = files ?? sourceFiles(root, config.ignore);
  for (const file of list) {
    const text = readFileSync(join(root, file), 'utf8');
    for (const finding of checkText(file, text, knowledge)) findings.push({ file: file.split(sep).join('/'), ...finding });
  }
  return {
    files: list.length,
    findings: findings
      .map(finding => ({ ...finding, level: levels[finding.rule] }))
      .filter(finding => finding.level !== 'off')
      .sort((a, b) => a.file.localeCompare(b.file) || a.line - b.line || a.column - b.column),
  };
}

