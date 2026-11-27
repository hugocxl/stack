# Changelog

## Unreleased

### Changed

- Draw all 2,000 vectors with an SF Symbols line language: a fine 1.05 px
  non-scaling stroke, three opacity tiers (1 and .9, .55, .32), continuous corners,
  edges that join their silhouettes, round-capped dashes measured on the canvas, and
  one stroke of clearance around badges, slashes and interlocking links.
- Warning triangles face the viewer like badges instead of lying in a side plane, and
  the notification bell has a smooth flared profile.
- Redraw every figure that failed an SF-grade review as a single designed object
  built from a few confident solids, among them success confirmation, sign-in,
  offline mode, trial period, monitoring, automation, collaboration and
  product inventory.
- Join the @hugocxl stack: the repository is now
  `hugocxl/vectors` and the website is https://hugocxl.github.io/stack/vectors/.
- Rebuild the website on the @hugocxl design system, with a home page, a
  searchable browser for all 2,000 vectors and a documentation page.
- `scripts/build.py` no longer writes `index.html` or `use-cases.html`; it still
  writes the SVGs and `catalog/manifest.json` and validates every use case.

### Added

- `@hugocxl/vectors` on npm: SVG strings (`/js`), React components (`/react`) and
  React Native components (`/react-native`), with per-vector, tree-shakeable ESM
  imports, TypeScript declarations and `catalog.json`. Components draw in
  `currentColor` by default and take `size` (width, with a 4:3 height) and `color`.
- The `Vectors` Swift package: a vector-preserving template asset catalog, the
  `Vector` enum and `image`, `uiImage` and `nsImage` helpers.
- `scripts/generate.py` with a `--check` mode, Node and Swift tests, and automatic
  npm and GitHub releases with provenance.
- `docs/USAGE.md`, the platform guide.

## First collection (unversioned)

### Added

- 2,000 static isometric SVG illustrations, published with a
  use-case manifest, a scene build and verification scripts.
