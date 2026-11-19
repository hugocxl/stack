# @hugocxl/ai

### One stack. Every agent builds it the same way.

Four libraries, designed to work as one, and the instructions that teach AI agents to use them
together. Whichever agent you work with (Claude Code, Codex, Cursor, Copilot, Gemini…) and
whichever project you start, the result follows the same rules.

| Library | What it does | Agent skill |
| --- | --- | --- |
| [@hugocxl/design-system](https://hugocxl.github.io/stack/design-system/) | Gives everything its type, color and space | `design-system` |
| [@hugocxl/icons](https://hugocxl.github.io/stack/icons/) | Labels what people can do | `icons` |
| [@hugocxl/vectors](https://hugocxl.github.io/stack/vectors/) | Illustrates what you mean | `vectors` |
| [@hugocxl/sounds](https://hugocxl.github.io/stack/sounds/) | Makes it feel like something | `sounds` |

## How it works

- **Each library ships its own skill** inside its npm package (`skills/<name>/SKILL.md`), so
  the instructions always match the version a project has installed. Icons and vectors include
  a catalog search, so agents look names up instead of guessing.
- **This package adds what no single library can say:** the
  [`stack` skill](skills/stack/SKILL.md) (which library covers which need, icon or vector, how
  colors and sounds pair with the design system, how to start a project) and the rules every
  project shares.
- **`npx @hugocxl/ai`** puts all of it into a project, keeps it current and checks the code.

## Set up a project

```sh
npm install @hugocxl/design-system @hugocxl/icons @hugocxl/vectors @hugocxl/sounds
npx @hugocxl/ai init
```

`init` writes:

- a managed section in **`AGENTS.md`**, read by Codex, Cursor, Copilot, Gemini and most other
  agents (anything you write outside the markers is kept);
- a **`CLAUDE.md`** that imports `AGENTS.md`, for Claude Code;
- the skills of the installed libraries, plus the `stack` skill, in **`.agents/skills/`** and
  **`.claude/skills/`**.

Commit them. After installing or upgrading a library, run `npx @hugocxl/ai sync`.

## Check a project

```sh
npx @hugocxl/ai check
```

It reads the catalogs of the installed libraries and reports:

| Rule | Level | Catches |
| --- | --- | --- |
| `agent-files` | error | `AGENTS.md`, `CLAUDE.md` or the skills missing or out of date with the installed libraries |
| `foreign-icons` | error | Lucide, Heroicons, Font Awesome, Material, Phosphor, react-icons and other icon libraries |
| `unknown-icon` | error | Icon names, styles, exports and import paths that do not exist |
| `unknown-vector` | error | Vector names, exports and import paths that do not exist |
| `unknown-sound` | error | Sounds and haptics that do not exist |
| `missing-library` | error | An `@hugocxl` library that is imported but not installed |
| `tailwind-palette` | warning | `bg-blue-500` and other Tailwind default colors next to the design system |
| `raw-color` | warning | Hex and `rgb()` colors in stylesheets next to the design system |

It exits with 1 on errors, so it works in CI and in an agent's own loop. `--strict` treats
warnings as errors and `--json` prints machine-readable findings. Configure it in
`package.json`:

```json
{
  "stack": {
    "rules": { "raw-color": "off", "tailwind-palette": "error" },
    "ignore": ["legacy/**"]
  }
}
```

A `stack-ignore` comment skips findings on its line, and `stack-ignore-next-line` on the next.

## Claude Code plugins

To have the skills in every Claude Code session without setting up each project, add the
[stack](https://github.com/hugocxl/stack) monorepo as a plugin marketplace:

```sh
claude plugin marketplace add hugocxl/stack
claude plugin install stack@hugocxl
```

`stack` installs the `design-system`, `icons`, `vectors` and `sounds` plugins with it. Each
library plugin comes straight from its latest npm release.

## Develop

`@hugocxl/ai` lives in [`ai/`](https://github.com/hugocxl/stack/tree/main/ai) of the
[stack](https://github.com/hugocxl/stack) monorepo, next to the four libraries.

```sh
pnpm install           # at the monorepo root
cd ai
pnpm test              # the CLI, the rules, the skill and the marketplace
pnpm run pack:check    # the files a publish would include
```

Every push to `main` that changes `ai/` and passes CI is released as `0.1.<run number>` to npm,
with provenance, and as a GitHub release tagged `ai-v<version>`.

## License

[MIT](LICENSE). Made by [Hugo](https://github.com/hugocxl).
