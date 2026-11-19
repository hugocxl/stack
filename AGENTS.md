# Working on @hugocxl/icons

Rounded icons in Duotone, Solid and Stroke, published as one npm package
(`packages/icons`: JS, React, React Native) and one Swift package (`Sources/Icons`).
[CONTRIBUTING.md](CONTRIBUTING.md) has the full development guide.

## Where things come from

```
scripts/icons/draw.py (+ full/, sf_*.py)  →  icons/*.svg, icons/styles/{solid,stroke}/*.svg, catalog.json
icons/ + catalog.json  →  scripts/generate.py  →  packages/icons/dist, Sources/Icons, docs/CATALOG.md
```

- Draw original artwork in the recipes, never by editing an SVG. The contract (one stroke
  width, one corner radius, selective duotone) is in [docs/DESIGN.md](docs/DESIGN.md) and
  [scripts/icons/STYLE.md](scripts/icons/STYLE.md).
- Everything under `packages/icons/dist`, `Sources/Icons/Resources` and `docs/CATALOG.md` is
  generated and committed. Run `npm run generate`; never edit it by hand.
- `docs/audit.json` binds a visual verdict to the hash of every SVG. Changed artwork fails
  validation until you render it, inspect it and update its entry. Never rehash without
  looking.
- Kind colors live in `scripts/icons/default-hues.json`.

## Check before you commit

```sh
npm ci
python -m pip install -r scripts/icons/requirements.txt
npm run validate        # artwork, review hashes, coverage, generation drift, tests, types, packing
npm run build:site && npm run check:site
```

Swift builds need macOS and Xcode; CI runs them.

## The agent skill

`packages/icons/skills/icons/` is what agents in other projects read: `SKILL.md` and
`scripts/search.mjs`. It ships in the npm package and is installed into projects by
[@hugocxl/stack](https://github.com/hugocxl/stack). When you change an import path, a prop,
a style or a name the skill mentions, update the skill in the same commit;
`tests/skill.test.mjs` checks every name and import in it.

## Releases and websites

Every push to `main` that passes CI publishes a new npm version, a GitHub release and a Swift
tag, then redeploys the websites that use the icons. Work on a branch and merge when it is
ready. Write commit messages as a short imperative sentence ("Add 189 icons covering…").
