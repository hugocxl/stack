// Build the components website into _site/: a React app made with @hugocxl/components
// itself, its stylesheet with the bundled fonts, and the Swift captures.
//
// Usage: node scripts/build-site.mjs [--serve]
import { cpSync, existsSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as esbuild from "esbuild";
import { themeScript } from "@hugocxl/components/react";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const out = join(root, "_site");
const serve = process.argv.includes("--serve");

rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });

const captures = existsSync(join(root, "website/swift"))
  ? readdirSync(join(root, "website/swift")).filter((file) => file.endsWith(".png")).sort()
  : [];
if (captures.length) cpSync(join(root, "website/swift"), join(out, "swift"), { recursive: true, filter: (path) => !path.endsWith(".DS_Store") });

writeFileSync(join(out, "index.html"), readFileSync(join(root, "website/index.html"), "utf8").replace("{{themeScript}}", themeScript));
writeFileSync(join(out, ".nojekyll"), "");

const options = {
  entryPoints: { app: join(root, "website/main.tsx") },
  outdir: out,
  bundle: true,
  format: "esm",
  jsx: "automatic",
  minify: !serve,
  sourcemap: serve,
  target: ["es2022"],
  loader: { ".woff2": "file", ".png": "file" },
  assetNames: "assets/[name]-[hash]",
  define: {
    "process.env.NODE_ENV": JSON.stringify(serve ? "development" : "production"),
    SWIFT_CAPTURES: JSON.stringify(captures.map((file) => `swift/${file}`)),
  },
  logLevel: "info",
};

if (serve) {
  const context = await esbuild.context(options);
  await context.watch();
  const { port } = await context.serve({ servedir: out, port: Number(process.env.PORT ?? 4322) });
  console.log(`Serving the components website at http://localhost:${port}/`);
} else {
  await esbuild.build(options);
  console.log(`Built _site for hugocxl.github.io/stack/components/ with ${captures.length} Swift captures.`);
}
