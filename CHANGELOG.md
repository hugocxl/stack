# Changelog

## Unreleased

### Changed

- Join the @hugocxl stack: the repository is now
  `hugocxl/vectors` and the website is https://hugocxl.github.io/vectors/.
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
