# Working on @hugocxl/vectors

2,000 isometric line illustrations, published as one npm package (`packages/vectors`: JS,
React, React Native) and the `Vectors` library of the `hugocxlStack` Swift package (`Sources/Vectors`, declared in the
monorepo root `Package.swift`).
[CONTRIBUTING.md](CONTRIBUTING.md) has the full development guide.

## Where things come from

```
scripts/scenes/ (+ redraws/) + catalog/use-cases.json  →  scripts/build.py  →  figures/*.svg, catalog/manifest.json
figures/ + catalog/manifest.json  →  scripts/generate.py  →  packages/vectors/dist, Sources/Vectors
```

- Draw a figure in a scene module, never by editing its SVG. A module in
  `scripts/scenes/redraws/` replaces a figure's composition; state badges come from
  `redraws/_kit.py`.
- The acceptance criteria (one subject, one state vocabulary, no people or words, 4:3,
  contrast in light and dark) are in [DESIGN.md](DESIGN.md). Use-case briefs are in
  [catalog/README.md](catalog/README.md).
- Everything under `packages/vectors/dist`, `Sources/Vectors/Resources` and
  `Sources/Vectors/Vector.swift` is generated and committed. Run `pnpm run generate`; never
  edit it by hand.

## Check before you commit

```sh
pnpm install
python -m pip install -r requirements.txt
python scripts/build.py --check --expect 2000
pnpm run validate        # SVG checks, generation drift, tests, types, packing, website
```

Swift builds need macOS and Xcode; CI runs them. Judge a drawing in a browser at 160 and
360 px on light and dark backgrounds; the mechanical checks cannot.

## The agent skill

`packages/vectors/skills/vectors/` is what agents in other projects read: `SKILL.md` and
`scripts/search.mjs`. It ships in the npm package and is installed into projects by
[@hugocxl/stack](https://github.com/hugocxl/stack). When you change an import path, a prop
or a name the skill mentions, update the skill in the same commit; `tests/skill.test.mjs`
checks every name and import in it.

## Releases and websites

Every push to `main` that changes `vectors/` and passes `.github/workflows/vectors.yml` publishes a new
npm version and a GitHub release tagged `vectors-v<version>`, then redeploys the stack website and
the other sites that use the vectors. Swift changes also pass `.github/workflows/swift.yml`, which
tags the `hugocxlStack` package with a plain `0.1.<run>` version. Work on a branch and merge when it is
ready. Write commit messages as a short imperative sentence ("Redraw 1,955 vectors…").
