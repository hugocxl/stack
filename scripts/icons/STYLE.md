# Drawing and contributing icons

Read [the design system](../../docs/DESIGN.md) for the visual contract, reference
roles, style definitions, compatibility rules, and review criteria. The measured
upstream conventions are preserved in [the legacy guide](../../docs/LEGACY_STYLE.md);
they apply to retained brand artwork, not the new rounded UI family.

## Authoring original UI artwork

Use `draw.py`: define a closed body with `shape`, or a linear composition with `glyph`. Linear glyphs default to one opaque tint;
never split a continuous mark into faded and primary pieces. Only a documented
foreground/background surface exception in `DUOTONE_GLYPHS` may use two tones. Use `rr`, `circle`, `path`, `line`, and `stroke` helpers.
Related icons should share a base and use deliberate identifying details. Do not
increase the count with arbitrary badge combinations or change a symbol's
meaning simply to reuse a drawing.

```sh
python3 -m venv /tmp/icons-artwork-venv
/tmp/icons-artwork-venv/bin/pip install -r scripts/icons/requirements.txt
/tmp/icons-artwork-venv/bin/python scripts/icons/draw.py
python3 -I scripts/icons/normalize.py icons
npm run generate
```

`draw.py --check` verifies that all original drawings and catalog entries match
the recipes. The check accepts a different ordering of otherwise byte-identical
closed contours within a path because Skia emits those in different orders on
Linux/x86 and macOS/ARM. Coordinates, commands, winding direction, layer order
and opacity must still match exactly; distributed SVG bytes and review hashes
remain strict. The pinned authoring dependencies are needed only for editing or
checking recipes; consuming SVGs and generating platform adapters use no Python
third-party packages. Canonical SVGs are checked in.

## SVG contract

- Lower kebab-case names, semantic nouns, consistent directional/state suffixes.
- SVG namespace, `fill="none"`, finite positive viewBox; no fixed width/height.
- Explicit `fill="currentColor"` on every path. Only numeric opacity layers.
- Expanded filled contours; no strokes, masks, filters, gradients, text, IDs,
  CSS, or external references. No background-colored cutouts.
- Canonical alphabetic attributes, two-space indentation, one path per line.
- `icons/NAME.svg` is the selective-Duotone default, including fully opaque
  linear symbols. `catalog.json` declares `defaultTone`; two tones are allowed
  only when they describe surfaces/depth. Other drawings live in
  `icons/styles/STYLE/NAME.svg`; `catalog.json` declares actual availability.
- Preserve upstream notices when adapting brands. Do not import proprietary
  reference artwork into this open library.

## Review and validation

```sh
swift scripts/icons/render-sheet.swift icons /tmp/icons-16.png --size 16 --scale 4
swift scripts/icons/render-sheet.swift icons/styles/solid /tmp/solid-32.png --size 32 --scale 2
swift scripts/icons/render-sheet.swift icons/styles/stroke /tmp/stroke-32.png --size 32 --scale 2
npm run validate
xcodebuild -scheme Icons -destination 'platform=macOS' test
xcodebuild -scheme Icons -destination 'generic/platform=iOS Simulator' CODE_SIGNING_ALLOWED=NO build
```

The native renderer shows light and dark tinting and fails on unloadable SVGs.
Split large review batches into temporary folders to stay within its bitmap-size
limit. Inspect the whole family and fix ambiguous or crowded symbols before
accepting a passing automated gate as sufficient.

## Full family audit

See [the review report](../../docs/REVIEW.md) and per-icon record. Run
`swift scripts/icons/render-audit.swift . review/final` for paginated category
sheets with every supported style, three sizes and two tints. Run
`python scripts/icons/test-design.py` in the authoring environment for topology
and symmetry regressions. `npm run validate` rejects stale review hashes. Inspect
changed rows before updating their records; never approve artwork by bulk
rehashing without looking at its rendered result.


## Full coverage recipes

The original expansion recipes live in `full/design.py`, `full/product.py`,
`full/technology.py`, and `full/world.py`. `draw.py` explicitly registers all four
when run as a command; importing it leaves the baseline available for isolated
review. `python scripts/icons/render-coverage.py GROUP` exports and renders a
group at 1x and 2x in the authoring environment on macOS. It never approves a
review or updates hashes.

Use `STYLE_OVERRIDES` for compositions whose surfaces require independent
occlusion or Solid counters. Their faded and opaque paths must not overlap,
and each linear mark stays opaque. Surface compositions stored as glyphs need
an explicit `DUOTONE_GLYPHS` rationale. A style override is not a visual approval.

`assemble-audit.py` combines explicit reviewer ledgers in precedence order and
rejects any stale SVG hash. The full audit keeps disagreements and their
coordinator adjudication available in separate source ledgers.

## SF-inspired additions

`sf_home.py`, `sf_media.py`, and `sf_accessibility.py` add original semantic
families through `draw.py`. Reference only concepts and optical design principles;
keep the existing stroke widths, corner language, and selective tone policy.

Reproduce the focused native review without changing its approval records:

```sh
python3 scripts/icons/render-focused.py docs/audit-sf-2026-11-17.json review/sf-expansion
```
