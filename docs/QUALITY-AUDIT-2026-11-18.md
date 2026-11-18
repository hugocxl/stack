# Single-weight redraw and quality audit · 18 November 2026

The owner flagged icons that were not good enough and set the bar: every icon
must look as if drawn by the same artist as Apple's SF Symbols, with the very
same stroke width and corner roundness throughout. Earlier audits had passed
icons that were clearly broken, so this audit changed the method, not just the
verdicts.

[Per-icon ledger](design-audit-2026-11-18.json) ·
[SF Symbols gap analysis](SF-GAP-2026-11-18.md)

## What was wrong

| Cause | Effect |
| --- | --- |
| A hierarchy of widths (1.35 lines, 1.25 outlines, 0.8–1.2 details) and arbitrary corner radii | Icons looked heavier than SF Symbols and as if drawn by several hands |
| Recipes scaled already-stroked geometry (`transform(line(...), scale=.65)`) | Inner chevrons, arrows and badges were visibly lighter than their containers |
| `add()` silently shrank 106 overflowing drawings | Every stroke in those icons thinned, up to 13.5% |
| Visual-only review | Weight mismatches, knots, fused parts and duplicated meanings passed |

## The contract

`draw.py` now enforces one stroke width, **1.1 units**, and one corner radius,
**1.25 units**, both measured from SF Symbols Regular rendered on this Mac and
scaled to the 16-unit grid. Every visible width passed to `stroke`, `line`,
`ring` or `outline` maps to 1.1; clearance cutters keep their widths. A radius
requested as a full pill stays a pill (capsules, toggles, microphones).

An automated gate rasterizes the Stroke style and opaque Duotone layer of every
drawing and measures stroke thickness along medial ridges. An icon passes when
its strokes measure 1.0–1.2 units with no counter lost against the original.

## Process

1. Five review agents graded all 2,152 drawings A/B/C in every style at 72, 24
   and 16 px: 966 A, 997 B, 189 C. All ten owner-flagged icons were caught.
2. Five fix agents, one per recipe file in its own git worktree, redrew C and B
   icons and every gate failure under the contract. The orchestrator compared
   every change before and after, rejected about 10–18% per round with a
   concrete redraw direction, and accepted only what read correctly in all styles.
3. Nine icons requested from the Tab interface were added:
   `circle-list-filter`, `rectangle-stack` (+`-plus`, `-minus`), `checklist`
   (+`-checked`, `-unchecked`), `sidebar-left`, `sidebar-right`.
4. After merging, five agents reviewed all 2,161 drawings again, grouped by
   category so families sat side by side. They failed 371; 289 were real defects
   (badge slots, near-square file and folder corners, frames changing width
   within a family, pinholes at 16 px, Solid variants losing fills, meanings such
   as `film` reading as a die). All were fixed in a final round and re-inspected.
   The remaining 82 were compatibility aliases or established synonym names kept
   for API stability; the ledger records each adjudication.

## Result

- 2,242 names: 2,161 original drawings and 81 brand marks.
- 2,161 of 2,161 drawings pass the single-weight gate.
- 2,242 of 2,242 names pass the hashed visual ledger (6,564 SVGs).
- 21 design regression tests, recipe check, normalization, Lucide coverage,
  generated adapters, package tests, type checks, site build and check,
  macOS `xcodebuild test` and the iOS Simulator build all pass.

Pass means no unresolved defect in this AI-assisted review against the design
contract. It is not an Apple endorsement or a human design certification. No SF
Symbols artwork was copied; real symbols were rendered only to measure weight,
radius and proportion.
