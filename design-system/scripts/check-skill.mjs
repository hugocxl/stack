// Checks that the agent skill shipped in skills/design-system matches the package:
// valid frontmatter, real export paths and the recipes the plan schema allows.
// Usage: node scripts/check-skill.mjs
import { readFileSync } from 'node:fs';

const root = new URL('../', import.meta.url);
const skill = readFileSync(new URL('skills/design-system/SKILL.md', root), 'utf8');
const manifest = JSON.parse(readFileSync(new URL('package.json', root), 'utf8'));
const schema = JSON.parse(readFileSync(new URL('system/plan.schema.json', root), 'utf8'));
const errors = [];

const front = skill.match(/^---\n([\s\S]*?)\n---\n/)?.[1] ?? '';
if (!/^name: design-system$/m.test(front)) errors.push('SKILL.md frontmatter must set name: design-system');
const description = front.match(/^description: (.+)$/m)?.[1] ?? '';
if (description.length < 50 || description.length > 1024) errors.push('SKILL.md description must be 50 to 1024 characters');

if (!manifest.files.includes('skills')) errors.push('package.json files must include skills');
for (const [, path] of skill.matchAll(/(?:pkg:)?@hugocxl\/design-system\/([a-z.-]+)/g)) {
  if (!(`./${path}` in manifest.exports)) errors.push(`SKILL.md names @hugocxl/design-system/${path}, which the package does not export`);
}

const recipes = skill.match(/\*\*Pick a recipe\*\* \(([^)]+)\)/)?.[1].match(/`([a-z]+)`/g)?.map(r => r.slice(1, -1)) ?? [];
if (recipes.join() !== schema.properties.recipe.enum.join()) errors.push(`SKILL.md recipes (${recipes}) differ from the plan schema (${schema.properties.recipe.enum})`);

if (errors.length) {
  console.error(errors.join('\n'));
  process.exit(1);
}
console.log('skills/design-system/SKILL.md matches the package.');
