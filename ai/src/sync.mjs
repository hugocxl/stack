// Write and verify the agent files a project gets from the stack: a managed section in
// AGENTS.md and a copy of each installed library's skill. No CLAUDE.md is created.
import { existsSync, lstatSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, join, relative } from 'node:path';
import { LIBRARIES, STACK_ROOT, libraries } from './project.mjs';

/** Where skills are copied. `.agents/skills` is read by most agents; Claude Code reads `.claude/skills`. */
export const SKILL_DIRS = ['.agents/skills', '.claude/skills'];
export const BEGIN = '<!-- @hugocxl/ai:begin — managed by `npx @hugocxl/ai sync`. Edit outside these markers. -->';
export const END = '<!-- @hugocxl/ai:end -->';
const MANAGED_IDS = ['stack', ...LIBRARIES.map(library => library.id)];

function filesIn(dir, base = dir) {
  return readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const path = join(dir, entry.name);
    return entry.isDirectory() ? filesIn(path, base) : [relative(base, path)];
  });
}

/** The managed section of AGENTS.md for these libraries. */
export function agentsSection(libs) {
  const rows = libs.map(library => {
    const use = library.installed ? `\`${library.package}\`` : `\`${library.package}\` (not installed: \`npm install ${library.package}\`)`;
    const skill = library.skillDir ? `\`${SKILL_DIRS[0]}/${library.id}\`` : library.installed ? 'upgrade the package to get its skill' : '—';
    return `| ${library.need} | ${use} | ${skill} |`;
  });
  const body = readFileSync(join(STACK_ROOT, 'templates/AGENTS.md'), 'utf8')
    .replace('{{libraries}}', rows.join('\n'))
    .replaceAll('{{skillsDir}}', SKILL_DIRS[0]);
  return `${BEGIN}\n${body.trimEnd()}\n${END}`;
}

function pruneEmpty(dir) {
  if (!existsSync(dir) || !lstatSync(dir).isDirectory()) return;
  for (const entry of readdirSync(dir)) pruneEmpty(join(dir, entry));
  if (readdirSync(dir).length === 0) rmSync(dir, { recursive: true });
}

/** AGENTS.md with its managed section added or replaced, keeping everything else. */
export function withSection(current, section) {
  if (current == null) return `# Agent instructions\n\n${section}\n`;
  const start = current.indexOf(BEGIN.slice(0, 26));
  const end = current.indexOf(END);
  if (start >= 0 && end > start) return current.slice(0, start) + section + current.slice(end + END.length);
  return `${current.trimEnd()}\n\n${section}\n`;
}

/** CLAUDE.md that imports AGENTS.md, keeping anything already in it. */
export function withImport(current) {
  if (current == null) return '@AGENTS.md\n';
  if (/^@AGENTS\.md\s*$/m.test(current)) return current;
  return `@AGENTS.md\n\n${current}`;
}

/** Every file the stack manages in `root`, with the content it should have. */
export function desiredFiles(root) {
  const libs = libraries(root);
  const files = new Map();
  const read = path => (existsSync(path) ? readFileSync(path, 'utf8') : null);

  files.set('AGENTS.md', withSection(read(join(root, 'AGENTS.md')), agentsSection(libs)));

  const sources = [{ id: 'stack', skillDir: join(STACK_ROOT, 'skills/stack') }, ...libs.filter(library => library.skillDir)];
  for (const base of SKILL_DIRS) {
    for (const { id, skillDir } of sources) {
      for (const file of filesIn(skillDir)) files.set(join(base, id, file), readFileSync(join(skillDir, file)));
    }
  }
  return { libs, files };
}

/**
 * Compare the project with what the stack wants. Returns the files to write and the files to
 * delete (managed skill files whose library or source file is gone).
 */
export function plan(root) {
  const { libs, files } = desiredFiles(root);
  const write = [];
  for (const [path, content] of files) {
    const target = join(root, path);
    const current = existsSync(target) ? readFileSync(target) : null;
    if (!current || !current.equals(Buffer.from(content))) write.push({ path, content, created: !current });
  }
  const remove = [];
  for (const base of SKILL_DIRS) {
    for (const id of MANAGED_IDS) {
      const dir = join(root, base, id);
      if (!existsSync(dir)) continue;
      for (const file of filesIn(dir)) {
        const path = join(base, id, file);
        if (!files.has(path)) remove.push({ path });
      }
    }
  }
  return { libs, write, remove };
}

/** Bring the project's agent files up to date. */
export function sync(root) {
  const result = plan(root);
  for (const { path, content } of result.write) {
    mkdirSync(dirname(join(root, path)), { recursive: true });
    writeFileSync(join(root, path), content);
  }
  for (const { path } of result.remove) rmSync(join(root, path));
  for (const base of SKILL_DIRS) for (const id of MANAGED_IDS) pruneEmpty(join(root, base, id));
  return result;
}
