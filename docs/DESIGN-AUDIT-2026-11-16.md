# Quality audit — 16 November 2026

Historical first-expansion report. See [the completed full audit](DESIGN-AUDIT-FULL.md) for the current catalog.

This audit reassesses every original catalog name and reviews a first
original coverage expansion. It supersedes the November 10 and 11 visual verdicts;
those records remain historical evidence. This is an AI visual assessment by
GPT-6.1 Sol and Terra at high reasoning effort, with coordinator review, not
independent human design certification.

## Inspection and acceptance

Every supported style is inspected at 16, 24 and 32 points, in light and dark
tints, at both 1× and 2× AppKit rasterization. Review covers semantic recognition,
optical balance, line weight, corners, contour continuity, small counters,
overlapping surfaces, badge clearance and coherence between related states.
A valid SVG or passing test does not establish design quality.

The complete baseline covered **550 names / 1,488 SVGs**: **527 passed,
13 failed and 10 needed review**. Two reviewers inspected disjoint categories;
corrections were re-rendered and assessed separately. Intermediate attempts were
rejected where problems remained, including folder corner wedges and C++ counters.

- [Searchable current visual report](design-audit-2026-11-16.html)
- [Complete current ledger](design-audit-2026-11-16.json)
- Baseline ledgers: [A](audit-2026-11-16-a.json), [B](audit-2026-11-16-b.json)
- Correction ledgers: [A](audit-2026-11-16-corrections-a.json), [B](audit-2026-11-16-corrections-b.json)
- [Expansion review](audit-2026-11-16-expansion.json)

Each current entry records its verdict, rationale, supported styles, exact SVG
SHA-256 hashes and native evidence paths. Local PNG evidence is under `review/`
(ignored by Git); the HTML previews use checked-in SVGs and remain portable.
The HTML is a review aid, not evidence of browser visual verification.

## Corrections

22 existing names changed across 46 SVGs.

- Battery charge is positive ink in every style; empty no longer reads as full
  in Solid. The charging variant follows the same state convention.
- Bicycle handlebars connect to their stem. Casting waves clear the display frame.
- Headphones retain an open headband. QR finder centers survive in Stroke.
- Folder Search keeps its magnifier clear of the frame. Folder Open uses a clean
  foreground flap with only the visible rear tab and upper contour in Stroke.
- Swatch separates overlapping leaves; Rainbow retains distinct bands in Solid.
- User status badges have intentional clearance from the shoulders.
- Calendar Range has endpoint cues; Git Compare has clear opposing routed arrows.
- Pipette has a bulb-shaped head; Podcast has separated broadcasting arcs.
- C++ retains its hexagonal mark with larger, separated counters. GraphQL retains
  every original node and edge, proportionately enlarged within its existing tile.

Eye Off, Hard Drive, Simulator and SSH received explicit contextual adjudication:
their silhouettes are coherent conventional or domain-specific abstractions,
without a demonstrated construction failure. A label may still be appropriate
for unfamiliar actions; passing the visual rubric is not a usability-study result.

## Expansion and coverage boundary

The accepted slice adds **29 original names / 87 SVGs**, bringing the catalog to
**579 names / 1,575 SVGs**. All 579 current names pass this visual rubric.
The proposed `handshake` was deferred after three revisions remained ambiguous
at 16 points; its rejected evidence is retained in the expansion ledger.

The first original-design slice adds useful concepts across accessibility,
healthcare, travel, animals, food, appliances, finance and tools. Each addition
uses the existing authoring helpers and is exported to SVG, JavaScript, React,
React Native and Swift, with all three styles.

This slice does **not** achieve Lucide parity. The [coverage report](COVERAGE-2026-11-16.md)
pins the official Lucide 1.73.0 inventory of 2,055 canonical names, distinguishes
strong semantic coverage from contextual name collisions, and assigns every
remaining gap to an implementation batch. Exact name matches are not automatically
equivalent states. Brands and compatibility duplicates do not inflate coverage.
Further expansion should proceed in individually reviewed 20–40-icon slices.

## Regression protection and reproduction

The current review gate validates complete catalog/style coverage and exact hashes.
It retains unresolved verdicts honestly; `--strict-design` additionally fails if
any name is failed or still needs review. The assembly utility only merges inspected
records and rejects stale hashes; it cannot manufacture approval or refresh hashes.

```sh
python3 scripts/icons/assemble-audit.py
python3 -I scripts/icons/check-review.py --strict-design
swift scripts/icons/render-audit.swift . review/current
python3 -m venv /tmp/icons-quality-venv
/tmp/icons-quality-venv/bin/pip install -r scripts/icons/requirements.txt
/tmp/icons-quality-venv/bin/python scripts/icons/draw.py --check
/tmp/icons-quality-venv/bin/python scripts/icons/test-design.py
npm run validate
xcodebuild -scheme Icons -destination 'platform=macOS' test
xcodebuild -scheme Icons -destination 'generic/platform=iOS Simulator' CODE_SIGNING_ALLOWED=NO build
```

New regression checks protect positive battery charge, badge clearance and syringe
connectivity, alongside the existing topology, symmetry, tone and counter checks.
Native review covers template rendering, not physical devices, arbitrary colors,
subpixel layout, React Native device rendering, trademark certification or human
recognition testing. No package publication is part of this change.

## Final local verification

The final 579-name catalog passed the strict visual-review hash gate, 16 design
regressions, deterministic recipe and generated-export checks, SVG normalization,
geometry/tone validation, 16 JavaScript tests, TypeScript checks and npm packaging
dry run. The coverage comparison reproduced its checked-in reports. The searchable
audit report passed DOM checks for 579 cards, 9,450 valid SVG previews, search and
verdict filtering. Four macOS Swift tests passed, including loading every style's
vector resources, and the generic iOS Simulator build succeeded. The README preview
was regenerated for all 579 names. Build/test logs are under
`review/quality-2026-11-16/` locally. No publication or remote CI result is claimed.
