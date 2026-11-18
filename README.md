# P9DS

A design system for text-led technical websites. Large reading type, hairline figures, mono labels and one scarce orange accent, on Superlogical’s paper and orange with neutral greys.

[Open the P9DS reference](https://hugocxl.github.io/p9ds/). One page holds the whole definition: tokens, layouts, thirteen components with live specimens and their markup, page recipes, rules and the agent handoff.

## Use the system

Copy `system/` into your site and add:

```html
<link rel="stylesheet" href="system/p9.css">
<script src="system/theme.js"></script>
<script type="module" src="system/p9.js"></script>
```

Set `class="p9"` and `data-layout="field"` (home) or `data-layout="plain"` (everything else) on the body. Then build the page from the recipe's components.

## Use it with an agent

Give the agent [DESIGN.md](DESIGN.md) at a pinned commit. It contains the same definition in Markdown, with each component's exact markup. For repeatable output, have the agent write a page plan that validates against [system/plan.schema.json](system/plan.schema.json), then render each block from its component markup.

## Assets and influences

- Self-hosted WOFF2 fonts from [Vercel Geist](https://vercel.com/font), npm release 1.9.2. See the [font license](system/fonts/Geist-LICENSE.txt).
- Interactive figures from [Hairline](https://github.com/lucasmarkes/hairline), version 0.5.1. The bundled vanilla module includes all 33 figures. See the [figure license](system/figures/LICENSE).
- Paper, orange, reading scale, column, field panel and footer from [Superlogical](https://www.superlogical.com/updates/public-testing-beginning). The greys are neutral rather than Superlogical’s green tint, and muted text meets WCAG AA. The field artwork is P9DS's own, in `system/images/`.

## Development

Run `python3 -m http.server 8000` and open `http://localhost:8000`. GitHub Pages publishes the root of main.

Specimens in `index.html` are the source of component markup. After editing one, run `npm run sync` to copy it into DESIGN.md. `npm test` lints DESIGN.md, checks that its markup matches the specimens, and runs the browser tests. For a first run, use `npm ci` and `npx playwright install chromium`.
