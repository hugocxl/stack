// Every recipe is built where it says it is, and nothing is built without a recipe.
//
// 1. Each recipe is complete and in a known group.
// 2. React: platforms.react is an export of @hugocxl/components/react (after pnpm run build).
// 3. Swift: platforms.swift is a public type in Sources/Components, with a gallery specimen
//    and a light and a dark capture in website/swift/.
// 4. Website: each recipe has examples, and a Swift snippet when it exists in Swift.
//
// Usage: node scripts/check-recipes.mjs
import assert from "node:assert/strict";
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const groups = ["foundations", "actions", "inputs", "feedback", "content", "layout"];
const fields = ["name", "title", "group", "summary", "use", "anatomy", "options", "states", "tokens", "rules", "accessibility", "platforms"];
const problems = [];

const recipes = readdirSync(join(root, "recipes"))
  .filter((file) => file.endsWith(".json"))
  .map((file) => ({ file, recipe: JSON.parse(readFileSync(join(root, "recipes", file), "utf8")) }));

// 1. Shape
const tokens = new Set(
  [...readFileSync(join(root, "node_modules/@hugocxl/design-system/dist/tokens.css"), "utf8").matchAll(/--ds-([\w-]+):/g)].map((m) => m[1]),
);
for (const { file, recipe } of recipes) {
  for (const field of fields) if (!(field in recipe)) problems.push(`${file}: missing ${field}`);
  if (`${recipe.name}.json` !== file) problems.push(`${file}: name is ${recipe.name}`);
  if (!groups.includes(recipe.group)) problems.push(`${file}: unknown group ${recipe.group}`);
  for (const token of recipe.tokens ?? []) if (!tokens.has(token)) problems.push(`${file}: --ds-${token} is not a design-system token`);
  if (!recipe.platforms?.react && !recipe.platforms?.swift) problems.push(`${file}: built nowhere`);
}

// 2. React
const react = await import(pathToFileURL(join(root, "packages/components/dist/react/index.js")).href);
const helpers = new Set(["ButtonGroup", "Muted", "Accent", "useTheme", "themeScript", "cx"]);
const reactNames = new Set(recipes.map(({ recipe }) => recipe.platforms.react).filter(Boolean));
for (const name of reactNames) if (!(name in react)) problems.push(`React: ${name} is not exported`);
for (const name of Object.keys(react)) {
  if (!reactNames.has(name) && !helpers.has(name)) problems.push(`React: ${name} is exported but no recipe names it`);
}

// 3. Swift
const swiftSources = readdirSync(join(root, "Sources/Components"))
  .filter((file) => file.endsWith(".swift"))
  .map((file) => readFileSync(join(root, "Sources/Components", file), "utf8"))
  .join("\n");
const gallery = readFileSync(join(root, "Sources/Components/Gallery.swift"), "utf8");
for (const { recipe } of recipes) {
  const name = recipe.platforms.swift;
  if (!name) continue;
  if (!new RegExp(`public (struct|enum) ${name}\\b`).test(swiftSources)) problems.push(`Swift: no public type ${name}`);
  if (!gallery.includes(`case "${recipe.name}":`)) problems.push(`Swift: no gallery specimen for ${recipe.name}`);
  for (const scheme of ["light", "dark"]) {
    if (!existsSync(join(root, "website/swift", `${recipe.name}-${scheme}.png`))) {
      problems.push(`Swift: no ${scheme} capture for ${recipe.name}; run pnpm run snapshots`);
    }
  }
}

// 4. Website
const examples = readFileSync(join(root, "website/examples.tsx"), "utf8");
const block = (name) => {
  const start = examples.search(new RegExp(`^  "?${name}"?: \\{`, "m"));
  if (start < 0) return null;
  const rest = examples.slice(start + 1);
  const end = rest.search(/^  "?[\w-]+"?: \{/m);
  return end < 0 ? rest : rest.slice(0, end);
};
for (const { recipe } of recipes) {
  const entry = block(recipe.name);
  if (!entry) problems.push(`Website: no examples for ${recipe.name}`);
  else if (recipe.platforms.swift && !/^    swift: /m.test(entry)) problems.push(`Website: no Swift snippet for ${recipe.name}`);
}

assert.deepEqual(problems, [], `Recipes and implementations disagree:\n  ${problems.join("\n  ")}`);
console.log(
  `${recipes.length} recipes: ${reactNames.size} in React, ${recipes.filter(({ recipe }) => recipe.platforms.swift).length} in Swift, all on the website.`,
);
