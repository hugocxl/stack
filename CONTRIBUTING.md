# Contributing to @hugocxl/vectors

## Development and validation

Use Node 22+, npm, Python 3.10–3.13 for the figure build (Python 3 with only the
standard library for everything else), and Xcode with Swift 6+ for Apple builds.

```sh
npm ci
npm run generate       # regenerate the npm and Swift packages from figures/
npm run validate       # SVG checks, generation drift, tests, types, packaging, website
swift test             # or: xcodebuild -scheme Vectors -destination 'platform=macOS' test
```

`npm run validate` runs `scripts/validate.sh`: `scripts/verify.py`,
`scripts/generate.py --check`, `npm test`, `npm run typecheck`, a dry-run
`npm pack` and the website build and link check.

## Drawing and building figures

The scene definitions live in `scripts/scenes/`. `scripts/build.py` projects their
3D coordinates into SVG, removes hidden lines and writes `figures/*.svg` and
`catalog/manifest.json` (from `catalog/use-cases.json`). It needs Shapely.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/build.py --expect 2000
python scripts/build.py --check --expect 2000
python scripts/verify.py --expect 2000 --similarity .965
npm run generate
```

`figures/` is the source of truth for distribution. See [DESIGN.md](DESIGN.md) for
the acceptance criteria and [catalog/README.md](catalog/README.md) for use-case
briefs.

## Generated files

`scripts/generate.py` writes, from `figures/` and `catalog/manifest.json`:

- `packages/vectors/dist/js`, `dist/react`, `dist/react-native`: one ESM module
  and declaration per illustration plus an index for each adapter.
- `packages/vectors/dist/catalog.json` and `packages/vectors/LICENSE`.
- `Sources/Vectors/Resources/Vectors.xcassets` (vector-preserving template
  images) and `Sources/Vectors/Vector.swift`.

Commit generated files so consumers need no Python or generation step. Never edit
them by hand; `npm run check` (`generate.py --check`) fails on any drift, and
`npm pack` runs it before packing. `Sources/Vectors/Images.swift` is hand-written.

## Website

The site is built from `website/` and `docs/USAGE.md` into `_site/` (ignored):

```sh
npm run build:site
npm run check:site           # links, anchors and assets
npx serve _site              # or any static server
```

The design system and the interface icons are dev dependencies, not copies:
the build copies `system/` from `@hugocxl/design-system` into `_site/system/` and
inlines each `{{icon name}}` placeholder in `website/*.html` (and the theme button)
from the stroke icons of `@hugocxl/icons`. The vectors are this repo's own
`figures/`. The Pages workflow installs the latest release of both packages
before building, so a design system release that triggers it redeploys the site
with the newest versions. Site-specific styles live only in `website/site.css`
and use only `--ds-*` tokens.

## Automatic releases

Every push to `main` runs the JavaScript and Apple checks, publishes the npm
package with provenance, verifies its registry integrity, then creates a GitHub
release with a Swift Package Manager tag, the npm tarball, SHA-256 checksums and
generated release notes. Pull requests and other branches only validate. A failed
check prevents publication. Push runs are not cancelled by newer pushes.

Versions use `0.1.<GitHub workflow run number>` (for example, `v0.1.12`). This
keeps versions unique without bot commits to `main`; numbers can have gaps due to
pull requests or failed runs. Retrying the same run reuses its version, recovers
an incomplete draft and leaves an already published release intact. The tag
points to the exact validated commit. The npm tarball manifest and its lockfile
workspace entry are stamped during packaging; the source manifest keeps the
development version. Change the `0.1` line in `scripts/prepare-release.mjs` when
planning a minor or major version change.

Publishing uses npm trusted publishing (OIDC) from `validate.yml`, with
`id-token: write` and a compatible npm CLI on Node 24. The package must authorize
`hugocxl/vectors` and this workflow file on npm; no npm token is stored in GitHub.
The first version of `@hugocxl/vectors` must exist before trust can be
configured, so that one-time bootstrap needs the npm owner's login. The GitHub
release uses `GITHUB_TOKEN` with `contents: write`; repository rules must permit
version tags.

Retries verify and skip an already published npm version. An integrity mismatch or
publication failure stops the GitHub release. Rerun a failed workflow to recover a
release interrupted after npm publication.

The website deploys from `pages.yml` on every push to `main`. GitHub Pages must be
set to deploy from GitHub Actions.
