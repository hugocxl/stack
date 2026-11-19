# Working on the stack monorepo

A pnpm workspace with six independently published packages. Each folder has its own
`AGENTS.md` with its layout, checks and rules. Read it before changing that folder.

- `design-system/`: `@hugocxl/design-system`, the package and its reference page.
- `icons/`, `vectors/`: npm workspaces (`packages/<name>`) plus the Swift sources.
- `sounds/`: `@hugocxl/sounds` (`packages/sounds`) and its website.
- `components/`: `@hugocxl/components` (`packages/components`, React), the `Components` Swift
  library and their website, built from one recipe per component in `components/recipes/`.
- `ai/`: `@hugocxl/ai`, the CLI and the `stack` skill that teach agents to use the libraries
  together.
- `Package.swift`: the `hugocxlStack` Swift package (`Icons`, `Vectors`, `Components`). Its
  targets point into `icons/`, `vectors/` and `components/`. Swift tooling runs from the root.
- `.claude-plugin/marketplace.json`: the Claude Code marketplace (`stack` from `./ai`, the
  libraries from npm).
- `scripts/build-site.mjs`: builds every package's site into one `_site/` for
  hugocxl.github.io/stack.
- `.github/workflows/`: one workflow per package (path-filtered to its folder), `swift.yml`
  and `pages.yml`.

## Rules

- Use pnpm (`pnpm install` at the root), never npm, for installs. Releases still pack and
  publish with the npm CLI, because npm trusted publishing needs it.
- Keep packages independent. A library depends on another one's published npm version, not
  the workspace copy.
- A push to `main` that touches a folder releases that package. Work on a branch and merge
  when it is ready. Write commit messages as a short imperative sentence.
