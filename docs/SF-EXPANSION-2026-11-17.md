# SF-inspired expansion · 17 November 2026

35 original additions bring IconsCXL from 2,198 to **2,233 names**: 2,152 UI
icons in three styles and 81 retained brand marks. Three existing icons receive
small optical refinements. The rounded construction, 16-unit grid, stroke
weights, selective duotone treatment, and existing names/imports are preserved.

[Preview this batch](sf-expansion-2026-11-17.html) ·
[Focused review ledger](audit-sf-2026-11-17.json) ·
[Combined current audit](design-audit-2026-11-17.html)

## Additions

| Family | New icons |
| --- | --- |
| Home controls (15) | ceiling-fan, curtains, dishwasher, doorbell, dryer, garage, intercom, light-switch, oven, power-outlet, smart-lock, stove, thermostat, window-closed, window-open |
| Capture (6) | camera-burst, camera-metering, exposure-lock, focus-auto, focus-manual, motion-photo |
| Audio and playback (6) | audio-mono, audio-spatial, audio-stereo, audio-transcription, noise-cancellation, playback-speed |
| Accessibility and activity (8) | assistive-listening, audio-description, hearing-aid, person-hiking, person-running, person-seated, person-walking, wheelchair-active |

Related symbols share geometry deliberately: appliances have a common body and
control panel, focus modes use the same corners, mono/stereo share a speaker,
and body poses retain the same rounded limb treatment. Linear symbols stay
opaque. Physical housings carry the secondary tone where it clarifies a surface.

## Small refinements

- `zoom-in` and `zoom-out`: move the interior mark 0.2 grid units right/down to
  align with the lens center at (6.7, 6.7).
- `airplay`: keep a transparent gap around the foreground triangle in default
  and Stroke, matching the separation already present in Solid. The lower
  screen outline no longer crosses the triangle.

## Reference and authorship

Apple's [SF Symbols overview](https://developer.apple.com/sf-symbols/) and
[custom symbol guidance](https://developer.apple.com/documentation/technologyoverviews/custom-sf-symbols)
inform semantic coverage, optical balance, and legibility. All added paths are
original IconsCXL recipes; no Apple artwork, font outlines, or symbol assets are
included. This is a focused expansion, not a claim of complete SF Symbols
coverage or support for Apple's variable weights, font metrics, or animations.

Candidates equivalent to existing `images` and `timer` were omitted. During
review the ceiling fan was changed to a mounted side elevation, motion-photo
rays became orbital segments, and mono/stereo gained an explicit speaker source.
These changes made the meanings more distinct within the existing collection.

## Review and reproducibility

The focused ledger records per-icon findings and SHA-256 hashes for all 114
reviewed SVGs: 105 additions and nine variants belonging to the refined icons
(AirPlay Solid is unchanged). Every row was inspected using AppKit at 16/24/32
points, in both tints, at 1× and 2×. The combined ledger preserves earlier
assessments for untouched icons; this pass did not re-audit the full collection.
Review is an AI visual assessment, not human design certification.

```sh
python3 scripts/icons/render-focused.py docs/audit-sf-2026-11-17.json review/sf-expansion
python3 scripts/icons/assemble-audit.py
python3 scripts/icons/check-review.py --strict-design
```

Editable additions live in `scripts/icons/sf_home.py`, `sf_media.py`, and
`sf_accessibility.py`, registered by `draw.py`. Regeneration updates the SVGs,
JS/React/React Native adapters, Swift enums and asset resources, catalog, and
offline gallery. The website derives its UI icon count from the catalog.

Native review PNGs are reproducible under ignored `review/sf-expansion/`; the
committed focused HTML previews the current SVGs in the same style/size matrix.

## Validation

- 17 geometry/design regressions passed; canonical recipe check passed.
- Strict review: 2,233 names, 6,537 SVGs, zero unresolved findings.
- `npm run validate`: artwork, generation drift, all 16 JavaScript tests, React /
  React Native type checks, package dry-run, and complete pinned Lucide coverage passed.
- `npm run build:site`: built successfully with 2,233 icons.
- macOS Xcode tests passed (four resource/API tests); iOS Simulator build passed.

These are local checks. A running React Native device app was not exercised,
and no commit, push, package publication, or public-site deployment was performed.
