// Build the package: TypeScript to dist/react, the stylesheet and the recipes.
import { execFileSync } from "node:child_process";
import { cpSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const dist = join(here, "dist");
rmSync(dist, { recursive: true, force: true });
execFileSync(join(here, "node_modules/.bin/tsc"), ["-p", here], { stdio: "inherit" });

// components.css is the components alone; styles.css adds the design-system fonts and tokens.
const css = readFileSync(join(here, "src/components.css"), "utf8");
writeFileSync(join(dist, "components.css"), css);
writeFileSync(
  join(dist, "styles.css"),
  `@import "@hugocxl/design-system/fonts.css";\n@import "@hugocxl/design-system/tokens.css";\n@import "./components.css";\n`,
);

const recipesDir = join(here, "../../recipes");
mkdirSync(join(dist, "recipes"), { recursive: true });
const recipes = readdirSync(recipesDir)
  .filter((file) => file.endsWith(".json"))
  .sort()
  .map((file) => {
    cpSync(join(recipesDir, file), join(dist, "recipes", file));
    return JSON.parse(readFileSync(join(recipesDir, file), "utf8"));
  });
writeFileSync(join(dist, "recipes.json"), JSON.stringify(recipes, null, 2) + "\n");
console.log(`Built @hugocxl/components with ${recipes.length} recipes.`);
