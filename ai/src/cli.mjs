import { relative } from 'node:path';
import { check, RULES } from './check.mjs';
import { findRoot, stackVersion } from './project.mjs';
import { SKILL_DIRS, sync } from './sync.mjs';

const HELP = `Usage: stack <command> [options]

Set up a project so every AI agent uses the @hugocxl stack the same way.

Commands:
  init     Set up the agent files: a stack section in AGENTS.md, a CLAUDE.md that
           imports it, and the skills of the installed libraries
  sync     Update the agent files after installing or upgrading a library
  check    Check the project follows the stack (exit 1 on errors)

Options:
  --cwd <dir>   Run in another directory (default: the nearest package.json)
  --json        check: print findings as JSON
  --strict      check: treat warnings as errors
  -v, --version Print the version
  -h, --help    Show this help

Rules for check (set one to "off", "warning" or "error" under "stack.rules" in
package.json, and skip paths with "stack.ignore" globs or a stack-ignore comment):
${Object.entries(RULES).map(([rule, { level, summary }]) => `  ${rule.padEnd(17)} ${level.padEnd(8)} ${summary}`).join('\n')}
`;

function parse(argv) {
  const options = { command: null, cwd: process.cwd(), json: false, strict: false };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--cwd') options.cwd = argv[++i];
    else if (arg === '--json') options.json = true;
    else if (arg === '--strict') options.strict = true;
    else if (arg === '-h' || arg === '--help') options.command = 'help';
    else if (arg === '-v' || arg === '--version') options.command = 'version';
    else if (!arg.startsWith('-') && !options.command) options.command = arg;
    else throw new Error(`Unknown option: ${arg}`);
  }
  return options;
}

function printSync(root, result, log) {
  for (const { path, created } of result.write) log(`  ${created ? 'created' : 'updated'}  ${path}`);
  for (const { path } of result.remove) log(`  removed  ${path}`);
  if (!result.write.length && !result.remove.length) log('  Agent files are already up to date.');
  const missing = result.libs.filter(library => !library.installed);
  const old = result.libs.filter(library => library.installed && !library.skillDir);
  const installed = result.libs.filter(library => library.skillDir).map(library => `${library.package}@${library.version}`);
  if (installed.length) log(`\nSkills from ${installed.join(', ')} are in ${SKILL_DIRS.join(' and ')}.`);
  if (old.length) log(`\nUpgrade to get their skills: npm install ${old.map(library => `${library.package}@latest`).join(' ')}`);
  if (missing.length) log(`\nNot installed yet: npm install ${missing.map(library => library.package).join(' ')}`);
}

export async function main(argv, { log = console.log, error = console.error } = {}) {
  let options;
  try {
    options = parse(argv);
  } catch (err) {
    error(err.message);
    error(HELP);
    return 2;
  }
  const root = findRoot(options.cwd);

  switch (options.command) {
    case 'version':
      log(stackVersion());
      return 0;
    case null:
    case 'help':
      log(HELP);
      return options.command ? 0 : 2;
    case 'init':
    case 'sync': {
      log(`@hugocxl/stack ${options.command} in ${relative(process.cwd(), root) || '.'}`);
      printSync(root, sync(root), log);
      if (options.command === 'init') {
        log('\nCommit AGENTS.md, CLAUDE.md and the skill folders. Before finishing any task, agents run:');
        log('  npx @hugocxl/stack check');
      }
      return 0;
    }
    case 'check': {
      const { files, findings } = await check(root);
      const level = finding => (options.strict && finding.level === 'warning' ? 'error' : finding.level);
      const errors = findings.filter(finding => level(finding) === 'error').length;
      const warnings = findings.length - errors;
      if (options.json) {
        log(JSON.stringify({ files, errors, warnings, findings: findings.map(finding => ({ ...finding, level: level(finding) })) }, null, 2));
      } else {
        for (const finding of findings) {
          log(`${finding.file}:${finding.line}:${finding.column}  ${level(finding).padEnd(7)}  ${finding.message}  (${finding.rule})`);
        }
        log(`${findings.length ? '\n' : ''}Checked ${files} file${files === 1 ? '' : 's'}: ${errors} error${errors === 1 ? '' : 's'}, ${warnings} warning${warnings === 1 ? '' : 's'}.`);
      }
      return errors ? 1 : 0;
    }
    default:
      error(`Unknown command: ${options.command}\n`);
      error(HELP);
      return 2;
  }
}
