# Contributing to Icons

## Development and validation

Use Node 22+, npm, Python 3, and Xcode with Swift 6+ for Apple builds.

```sh
npm ci
npm run generate       # regenerate adapters after editing icons/
npm run validate       # artwork, generation drift, rendering, types, packaging
xcodebuild -scheme Icons -destination 'platform=macOS' test
xcodebuild -scheme Icons -destination 'generic/platform=iOS Simulator' CODE_SIGNING_ALLOWED=NO build
```

`icons/` is the source of truth for distribution. Original editable recipes live
in `scripts/icons/draw.py`; see the drawing guide for pinned authoring tools. Commit generated `packages/*/dist` and
`Sources/Icons` resources so consumers do not need Python or a generation
step. Do not edit generated files directly. Build caches and dependencies are
ignored. CI validates JavaScript packages on Linux and Swift on macOS, including
an iOS Simulator build. Use Xcode for asset-catalog tests; standalone SwiftPM resource compilation varies
with the installed toolchain. Device rendering and a running React Native app still
need app-level verification.

### Automatic releases

Every push to `main` runs the JavaScript and Apple checks, publishes the single npm
package with provenance, verifies its registry integrity, then creates a GitHub
release with a Swift Package Manager tag, the npm package tarball, SHA-256
checksums, and generated release notes. Pull requests and other branches only
validate. A failed check prevents publication. Push runs are not cancelled by
newer pushes.

Versions use `0.1.<GitHub workflow run number>` (for example, `v0.1.12`). This
keeps versions unique without bot commits to `main`; numbers can have gaps due
to pull requests or failed runs. Retrying the same run reuses its version,
recovers an incomplete draft, and leaves an already published release intact.
The tag points to the exact validated commit. npm tarball manifests and their
lockfile workspace entries are stamped during packaging; source manifests keep
the development version. Change the `0.1` release line in
`scripts/prepare-release.mjs` when planning a minor or major version change.

Publishing uses npm trusted publishing (OIDC) from `validate.yml`, with
`id-token: write` and a compatible npm CLI on Node 24. The package authorizes
`hugocxl/icons` and this workflow filename on npm. No npm token is stored in
GitHub. The GitHub release uses `GITHUB_TOKEN` with `contents: write`; repository
rules must permit version tags. The initial package must exist before trust
can be configured; that one-time bootstrap requires the npm owner's login.

Retries verify and skip an already published npm version. An integrity mismatch or publication failure stops the
GitHub release. All three adapters share one version and one tarball; rerun a failed workflow
to recover a release interrupted after npm publication.

## Contribute

Icons grew out of the icon collection adapted and extended for
[Tab](https://github.com/hugocxl/tab).

See [the drawing guide](scripts/icons/STYLE.md) for geometry and naming conventions.
Tools use Python 3's standard library; the contact sheet requires Swift and AppKit
on macOS.

```sh
python3 -I scripts/icons/normalize.py icons
python3 -I scripts/icons/test-adapt-brand.py
preview_dir=$(mktemp -d)
while IFS= read -r name; do cp "icons/$name.svg" "$preview_dir/"; done < scripts/icons/preview.txt
swift scripts/icons/render-sheet.swift "$preview_dir" preview.png --size 24 --scale 2 --columns 8
rm -r "$preview_dir"
scripts/validate.sh
```

The importer and brand adapter in `scripts/icons/` help prepare new artwork.
Preserve upstream attribution when adapting artwork.

