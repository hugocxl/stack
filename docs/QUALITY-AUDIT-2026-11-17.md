# Full catalog quality audit · 17 November 2026

Fresh visual review of **all 2,233 names and all 6,537 supported SVG variants**.
The audit corrected **233 names / 659 SVG variants**, preserving icon names,
style availability and public exports.

[Before and after, every correction](quality-changes-2026-11-17.html) ·
[Full searchable review](design-audit-2026-11-17.html) ·
[Per-icon ledger](design-audit-2026-11-17.json)

## What was wrong

The supplied badge examples were valid SVGs but inconsistent drawings. Badge
Plus, Sterling, Question Mark and Check used different seal outlines; the question
mark crowded the upper border, and currency strokes were visibly lighter than
nearby status marks. Earlier passing reviews had not caught these problems.
This audit supersedes those visual assessments rather than carrying them forward.

| Finding | Applied correction |
| --- | --- |
| Uneven and incompatible badge silhouettes | One symmetric eight-point seal across all 18 badges, with fitted interior marks and consistent currency weight. |
| Interior marks touching their containers | Rebalanced currency circles, help marks, circular alphabet, file/folder details, cloud arrows and backup clocks. |
| Artificial edges around status marks and disabled slashes | Build the complete object first, then clip its rendered layers behind the foreground mark; retain transparent separation in every style. |
| Solid conversion losing identifying details | Restore gift ribbons, both construction stripes, sofa seams, guitar details and status symbols; separate stacked objects and people. |
| Fused or malformed geometry | Repair cog symmetry, group heads, voicemail reels, waypoint counters, reply-all arrows, insertion controls, club/clover lobes and cuboid perspective. |
| Incorrect state meaning | Give half-filled shapes a true half-filled treatment; preserve directional symmetry and distinct foreground/background planes. |
| Small rendering defects | Remove protruding keyboard keys and circular-rim marks, clear printer labels and book arrows, and open the life-buoy center. |

The shared status-badge fix initially left an overlap in `image-upscale`.
The geometry gate caught it. Its clearance now covers the entire foreground
mark, and the affected family was rendered and inspected again before acceptance.

## Review coverage

| Scope | Names reviewed | Changed |
| --- | ---: | ---: |
| Baseline UI, earlier expansion and retained brands | 579 | 12 |
| Design, layout, typography and navigation additions | 565 | 48 |
| Product interfaces and recent SF-inspired additions | 462 | 97 |
| Technology, world, media, sport and commerce additions | 627 | 76 |
| **Total** | **2,233** | **233** |

Each supported style was inspected in native AppKit matrices at **16, 24 and
32 points**, in **light and dark**, at **1× and 2×**. Unchanged rows were inspected
fresh; changed drawings were regenerated and inspected again. Source recipes were
also checked for shared family constructions, structural connections, counters,
geometry intersections and deliberate occlusion. Changed product families received
an independent second review; the coordinator additionally reviewed all badges
together across categories.

The five `audit-quality-*.json` source ledgers record each name, supported styles,
findings, native evidence row/page and SHA-256 of the reviewed SVGs. The combined
ledger is assembled only when every hash matches the distribution assets.
Retained brands keep their source identities and attribution; no proprietary
SF Symbols artwork was imported.

Pass means no unresolved defect was identified in this AI-assisted review against
the library's design criteria. It is not an Apple endorsement or a guarantee of
perfect perception in every application. Dense brand details naturally soften at
16pt. Browser previews are provided for comparison; the stated native evidence
comes from AppKit, not browser scaling. Physical iOS devices and running React
Native applications were not part of this review.

## Validation

All integration checks passed:

- Recipe consistency and 25 geometry regression tests, including badge symmetry,
  container clearance, separated controls, cuboid edges and preserved Solid details.
- SVG normalization, 12 brand adaptation tests, finite geometry/bounds/tone checks,
  and exact review hashes for all 6,537 variants with zero unresolved findings.
- Pinned Lucide coverage: 2,055/2,055 concepts (1,971 exact names, 84 reviewed equivalents).
- `npm run validate`: generated-file consistency, 16 package/gallery tests,
  web and React Native type checks, and package dry run.
- macOS `xcodebuild test` and iOS Simulator `xcodebuild build`.
- `npm run build:site`: complete 2,233-icon gallery.

The public API and catalog counts remain unchanged. SVGs,
JavaScript/React/React Native adapters, Swift resources and the offline gallery
were regenerated from the recipes. These are local validation results; this
audit does not publish a package or release.

## Reproducing the review

Install the pinned authoring dependencies from `scripts/icons/requirements.txt`,
then run:

```sh
python scripts/icons/draw.py --check
python scripts/icons/test-design.py
python scripts/icons/test-quality-design.py
python scripts/icons/assemble-audit.py
npm run validate
python scripts/icons/render-focused.py docs/design-audit-2026-11-17.json review/quality-reproduced
```

The last command renders the complete current catalog at both raster scales.
It never grants approval or refreshes review hashes. Native evidence images are
local reproducible artifacts under `review/`; the committed ledgers and embedded
before/after HTML remain available without those images.
