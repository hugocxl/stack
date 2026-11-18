# Figure review

Every figure earns its place by illustrating a specific moment on a website. A use case can stay in the catalog while its illustration is still being developed.

## Acceptance criteria

- **Meaning.** At 160 CSS pixels, the silhouette and focal relationship support the intended heading. Check the difference between adjacent states such as search, no results, and offline.
- **Composition.** Give the viewer one place to look first. Leave breathing room around the artwork so a title or paragraph can sit beside it. Compare with its nearest neighbors in the library and reject repeated compositions that convey the same idea.
- **Construction.** At 360 CSS pixels, verify that parts attach where they appear to attach, solids conceal the correct edges, and details sit on the intended faces. Check locator guides, intersections, near tangencies, and the tips of directional marks.
- **Contrast.** Review each SVG on light and dark backgrounds at both sizes. Keep contours legible and construction lines visibly quieter. The art should leave the page background visible through every gap.
- **Delivery.** Export a standalone static SVG with a transparent 480 × 360 viewBox, a title, a description, and a stable filename. Run `python scripts/build.py --check` and verify that the use case links to its artwork.

Mechanical checks catch stale outputs and broken cross-references. Browser review is required to judge the drawing.

## Review of the original collection

All 50 original figures were reviewed in Chromium on both backgrounds at 160 and 360 CSS pixels. The first pass identified 15 compositions for redraw, 28 for refinement, and seven with a baseline worth preserving.

- Product architecture, Focus states, and Permissions previously relied on similar stacked forms. The revised scenes use an exploded assembly, a focused control, and keyed access.
- Collaboration and Handoff now put their shared work surface and transfer gap in view. Version control exposes both the fork and the merge.
- Data pipeline, Load balancing, and Failover now show their connections. Forecasting makes the split between observations and projections visible.
- Security has a single connected shackle, Privacy uses a physical shutter, and Conversion uses fewer openings so the taper reads at thumbnail size.

The expanded set went through a second browser pass. The changes from that pass included a clearer empty search panel, corrected checkmarks, distinct learning milestones, and aligned suspension points on the comparison scale.
