# stack

### Everything I build with, in one place.

The `@hugocxl` stack: six independently published libraries, the `@hugocxl/ai` CLI and agent skill, and the shared GitHub Actions workflows and script templates used across all `hugocxl/*` repositories.

[Visit the website](https://hugocxl.github.io/stack/) · [Install Claude plugin](#development)

## Highlights

- **Design system, icons, vectors, sounds, components.** One cohesive system across Web, React, React Native, and Swift (`hugocxlStack`).
- **Agent tooling (`@hugocxl/ai`).** Syncs library skills and checks code and repository hygiene with `npx @hugocxl/ai check`.
- **Shared CI & release automation.** Public reusable GitHub Actions workflows (`.github/workflows/reusable-*.yml`) and canonical script/hook templates (`templates/`) shared by all `hugocxl/*` repos.

| Folder | Package | What it does |
| --- | --- | --- |
| [`design-system/`](design-system) | [@hugocxl/design-system](https://hugocxl.github.io/stack/design-system/) | Type, color, spacing, and layout tokens |
| [`icons/`](icons) | [@hugocxl/icons](https://hugocxl.github.io/stack/icons/) | Rounded icons for web, React, React Native, and Swift |
| [`vectors/`](vectors) | [@hugocxl/vectors](https://hugocxl.github.io/stack/vectors/) | Isometric line illustrations for web, React, React Native, and Swift |
| [`sounds/`](sounds) | [@hugocxl/sounds](https://hugocxl.github.io/stack/sounds/) | Synthesized tactile interface sounds |
| [`components/`](components) | [@hugocxl/components](https://hugocxl.github.io/stack/components/) | React and Swift components built on the design system |
| [`ai/`](ai) | [@hugocxl/ai](https://hugocxl.github.io/stack/) | CLI, skills, and hygiene checks for AI agents |

## Development

Requires Node 22+, `pnpm` (pinned in `package.json`), Python 3.12 (for icon/vector builds), and Xcode with Swift 6+.

```sh
pnpm install
pnpm test
pnpm build:site && pnpm check:site
swift test
```

Use in another project:

```sh
npm install @hugocxl/design-system @hugocxl/icons @hugocxl/vectors @hugocxl/sounds
npx @hugocxl/ai init
claude plugin marketplace add hugocxl/stack && claude plugin install stack@hugocxl
```

## Releases

Each library releases independently on push to `main` via its path-filtered workflow in `.github/workflows/`, publishing to npm with trusted provenance and creating a `<folder>-v<version>` GitHub release. Commits follow `<Added|Changed|Removed|Improved|Fixed>: <One user-facing sentence.>` (enforced by `.githooks/commit-msg`).

## License

Each package carries its own `LICENSE` file. Made by [Hugo](https://github.com/hugocxl).
