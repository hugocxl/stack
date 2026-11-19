# stack

### Everything I build with, in one place.

The @hugocxl stack: four libraries designed to work as one, and the tooling that teaches AI
agents to use them together. Each one is published on its own and has its own README.

| Folder | Package | What it does |
| --- | --- | --- |
| [`design-system/`](design-system) | [@hugocxl/design-system](https://hugocxl.github.io/stack/design-system/) | Gives everything its type, color and space |
| [`icons/`](icons) | [@hugocxl/icons](https://hugocxl.github.io/stack/icons/) | Labels what people can do. 2,233 rounded icons for the web, React, React Native and Swift |
| [`vectors/`](vectors) | [@hugocxl/vectors](https://hugocxl.github.io/stack/vectors/) | Illustrates what you mean. 2,000 isometric line illustrations for the web, React, React Native and Swift |
| [`sounds/`](sounds) | [@hugocxl/sounds](https://hugocxl.github.io/stack/sounds/) | Makes it feel like something. Tactile interface sounds synthesized with Web Audio |
| [`ai/`](ai) | [@hugocxl/ai](https://hugocxl.github.io/stack/) | Sets up any project so every AI agent uses the stack the same way |

Website: **[hugocxl.github.io/stack](https://hugocxl.github.io/stack/)**, one section per library.

## Use it

```sh
npm install @hugocxl/design-system @hugocxl/icons @hugocxl/vectors @hugocxl/sounds
npx @hugocxl/ai init
```

**Swift.** `Icons` and `Vectors` ship together in the `hugocxlStack` Swift package, declared
in this repository's [`Package.swift`](Package.swift):

```swift
.package(url: "https://github.com/hugocxl/stack.git", from: "0.1.0")
// target dependencies: .product(name: "Icons", package: "stack"), .product(name: "Vectors", package: "stack")
```

**Claude Code.** This repository is also a plugin marketplace:

```sh
claude plugin marketplace add hugocxl/stack
claude plugin install stack@hugocxl
```

## Develop

A pnpm workspace. Node 22+, pnpm (the version in `package.json`), Python 3.12 for the icon and
vector builds, and Xcode with Swift 6+ for the Swift package.

```sh
pnpm install
pnpm test                     # every package's tests
pnpm build:site               # the combined website into _site/
pnpm check:site
swift test                    # the hugocxlStack Swift package
```

Work inside a package with `cd <folder>` and its own scripts; each folder's `AGENTS.md` says
how.

## Releases

Each library releases on its own. A push to `main` that changes a folder runs its workflow in
`.github/workflows/`; when it passes, the package is published to npm with provenance through
trusted publishing, and as a GitHub release tagged `<folder>-v<version>`. Then the website
redeploys.

| Package | Workflow | Versions |
| --- | --- | --- |
| @hugocxl/design-system | `design-system.yml` | `0.2.x` |
| @hugocxl/icons | `icons.yml` | `0.2.x` |
| @hugocxl/vectors | `vectors.yml` | `0.1.x` |
| @hugocxl/sounds | `sounds.yml` | `0.1.x` |
| @hugocxl/ai | `ai.yml` | `0.1.x` |
| hugocxlStack (Swift) | `swift.yml` | plain `0.1.x` tags |

## License

Each package carries its own license; see the `LICENSE` file in each folder. Made by
[Hugo](https://github.com/hugocxl).
