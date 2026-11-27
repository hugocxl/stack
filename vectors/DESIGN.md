# Figure review

Every figure earns its place by illustrating a specific moment on a website. A use case can stay in the catalog while its illustration is still being developed.

## Acceptance criteria

- **Meaning.** At 160 CSS pixels, the silhouette and focal relationship support the intended heading. Check the difference between adjacent states such as search, no results, and offline.
- **Composition.** Give the viewer one place to look first. Leave breathing room around the artwork so a title or paragraph can sit beside it. Compare with its nearest neighbors in the library and reject repeated compositions that convey the same idea.
- **Construction.** At 360 CSS pixels, verify that parts attach where they appear to attach, solids conceal the correct edges, and details sit on the intended faces. Check locator guides, intersections, near tangencies, and the tips of directional marks.
- **Contrast.** Review each SVG on light and dark backgrounds at both sizes. Keep contours legible and construction lines visibly quieter. The art should leave the page background visible through every gap.
- **Delivery.** Export a standalone static SVG with a transparent 480 × 360 viewBox, a title, a description, and a stable filename. Run `python scripts/build.py --check` and verify that the use case links to its artwork.

Mechanical checks catch stale outputs and broken cross-references. Browser review is required to judge the drawing.

## Line language

The collection draws like an extension of SF Symbols. `scripts/geometry.py` owns every rule, so a scene
module never sets a weight, a gap or a dash itself.

- **One weight.** Every stroke is 3.6 units on the 480 × 360 canvas and scales with the artwork, as a
  symbol's stroke does: about 1.2 points at 160 wide, 2.7 at 360. Caps and joins are round.
- **Hierarchy by opacity, not weight.** Outlines and badge glyphs are primary (1 and .9), interior
  detail is secondary (.55) and construction guides are tertiary (.32), after SF Symbols'
  hierarchical rendering.
- **Continuous corners.** Rounded rectangles use the squircle profile of Apple's icons: a corner
  eases into its edges over 1.42 radii instead of meeting them at a circular tangent. Corners that
  meet become a capsule.
- **Edges that join.** The near top edge of a solid runs into its silhouette, as the edges of SF's
  `cube` and `shippingbox` do. Hidden lines stop 0.35 units short of the part that hides them, so
  T-junctions read as joined, not crossed.
- **Clearance.** A badge, a slash or a link passing in front of another part clears it by about one
  stroke of air, the knockout of SF's `.badge`, `.slash` and `link` symbols. Use `knockout_layer` for
  a part in front and `interlace` for rings that pass over and under each other.
- **Short dashes.** Dashed lines are measured in output units: 1.05 strokes on, a 2.35-stroke period,
  spread to start and end on a dash, as in `circle.dashed`.
- **Glyphs.** State glyphs follow SF construction: right-angled arrowheads and a warning triangle with
  rounded corners.

## Symbol-level redraw

The library was audited against an SF Symbols bar: at 160 CSS pixels, a viewer who sees only the drawing names its concept. Most figures in the expansion packs paired generic props from a layout recipe and failed. The audit kept 45 figures and redrew the other 1,955, one module each in `scripts/scenes/redraws/`.

- **One subject.** Each figure draws the real-world object that denotes its concept, such as a tooth, a parcel locker or a funnel. It shows at most three objects, without filler trays or platforms.
- **One state vocabulary.** State is a badge that faces the viewer, so its glyph stays upright: check for done, x for failed, clock for pending, refresh for retry, plus for add, pause, lock and the warning triangle. Sibling states share an object and differ only by badge.
- **Object-only.** The figures contain no people, words or numerals. A single letter appears only when the letter is the concept, as in A/B testing.
- **Variety.** No single base form, such as a tilted document or a chart easel, carries more than about one figure in five within a group.

Every redraw was reviewed in Chromium at 160 and 360 CSS pixels on light and dark backgrounds, compared with its siblings, and sent back until it passed.

## Review at 2,000 figures

The build rejects self-intersecting projected faces and requires every catalog link to resolve to a shipped SVG. The release check also enforces the figure count, checks SVG elements and attributes, verifies all path coordinates and safe margins, and detects identical geometry. A normalized contour comparison surfaces near-duplicates for side-by-side review. Each file is rasterized in Chromium at 160 and 360 CSS pixels on light and dark backgrounds to check loading, visible ink, and clipping.

Visual review uses contact sheets and individual enlargements for new compositions, reported defects, and closely matched silhouettes. Related figures share objects and construction methods. Inspect the specific scene for meaning, depth, alignment, and line collisions before accepting a change.

Product return was redrawn after a reported defect. Two flaps fold from opposite rim edges, and the arrow follows a separate ground path with the arrowhead clear of the carton.

## Review of the original collection

All 50 original figures were reviewed in Chromium on both backgrounds at 160 and 360 CSS pixels. The first pass identified 15 compositions for redraw, 28 for refinement, and seven with a baseline worth preserving.

- Product architecture, Focus states, and Permissions previously relied on similar stacked forms. The revised scenes use an exploded assembly, a focused control, and keyed access.
- Collaboration and Handoff now put their shared work surface and transfer gap in view. Version control exposes both the fork and the merge.
- Data pipeline, Load balancing, and Failover now show their connections. Forecasting makes the split between observations and projections visible.
- Security has a single connected shackle, Privacy uses a physical shutter, and Conversion uses fewer openings so the taper reads at thumbnail size.

The expanded set went through a second browser pass. The changes from that pass included a clearer empty search panel, corrected checkmarks, distinct learning milestones, and aligned suspension points on the comparison scale.
