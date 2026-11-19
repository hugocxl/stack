---
name: design-system
description: Use @hugocxl/design-system for the look of every @hugocxl website, page and interface — type, color, spacing, layout, page recipes and the thirteen components. Covers reading the full definition (DESIGN.md), planning a page, rendering components exactly, and using the tokens from plain HTML, Tailwind, CSS, Sass or JavaScript. Use it whenever you create, style or review a page, a screen or a component.
---

# @hugocxl/design-system

The signature shared by every @hugocxl project: large reading type in Geist, quiet line
vectors, rounded Stroke icons, monospaced labels and one scarce orange accent. Flat, light and
dark, accessible by default.

## Read the definition first

`DESIGN.md` defines the system completely; anything it does not describe is not part of the
system. Read it before building or changing any page. It ships in the package:

- In a project: `node_modules/@hugocxl/design-system/DESIGN.md`
- Otherwise: `../../DESIGN.md` from this skill's directory

Its YAML front matter holds every token value. Its body holds the colors, type scale, layout,
page recipes, the markup of each component, and the rules.

## Build a page

1. **Pick a recipe** (`home`, `article`, `docs`, `changelog`, `pricing`, `contact`). It fixes
   the layout and the order of components.
2. **Write a page plan** for anything beyond a trivial page: JSON that validates against
   `@hugocxl/design-system/plan.schema.json`, naming the recipe, the layout and every block
   with its content. Check the block order against the recipe.
3. **Render each block** by copying the component's markup from DESIGN.md exactly. Change only
   text, links, IDs and the names of vectors and icons.
4. **Fill figures and icons** from `@hugocxl/vectors` and `@hugocxl/icons` (see their skills),
   never from anything else.
5. **Verify** at 320, 760, 761 and 1440 px wide in both themes.

Never invent copy, links, numbers, quotes or logos the brief does not supply. If a required
input is missing, ask for it.

## Install

```sh
npm install @hugocxl/design-system @hugocxl/icons @hugocxl/vectors
```

| Stack | Use |
| --- | --- |
| Static HTML (the reference) | Serve `system/` from the package. Load `system/ds.css` and `system/theme.js` in the head and `system/ds.js` as a module. Body: `class="ds"` and the recipe's `data-layout`. |
| Tailwind v4 | `@import "@hugocxl/design-system/tailwind";` |
| Tailwind v3 | `presets: [require('@hugocxl/design-system/tailwind-preset')]` |
| Plain CSS | `@hugocxl/design-system/fonts.css` and `@hugocxl/design-system/tokens.css` (custom properties `--ds-<role>`) |
| Sass | `@use "pkg:@hugocxl/design-system/scss";` |
| JavaScript | `import { tokens } from '@hugocxl/design-system/tokens'` or `@hugocxl/design-system/tokens.json` |

In Tailwind, use only the token utilities (`bg-canvas`, `text-ink`, `text-muted`,
`text-reading`, `p-space-5`, `rounded-media`, `max-w-measure`…). Never Tailwind's default
palette, font sizes, spacing or radii (`bg-blue-500`, `text-xl`, `p-4`, `rounded-lg`).

The theme follows the reader's preference and switches with `data-theme="light|dark"` on
`<html>`; `system/theme.js` sets it before the first paint.

## Rules that matter most

The full list is in DESIGN.md under "Do's and Don'ts". The ones agents break most often:

- **Tokens only.** No color, font, size, weight, radius or spacing value that is not a token.
  No hex values in components.
- **Accent at most twice per page:** the status dot (`.ds-dot`) and one phrase at title size
  (`.ds-accent`). Never on body text, links, buttons, backgrounds, rules, icons or figures.
- **Hue and status colors only on icons and dots**, and the words beside them always say what
  the color means.
- **Nothing larger than the title**, nothing bolder than 500. Sentence case. Left-aligned text;
  only the column is centered.
- **Flat.** No shadows, gradients, blur, emoji or stock imagery.
- **One filled button per page.**
- **Icons** use the Stroke style, sit only in links, the button, meta labels and icon buttons,
  and never replace words.
- **Figures** are vectors from `@hugocxl/vectors` in `figure-wide` or `figure-grid`, chosen for
  their meaning and named in the caption.
- **Accessible:** every icon button has an `aria-label`, every field a visible label, every
  image `alt` text, and every vector keeps its `title`.

## App screens and other stacks

For an app screen, a component library or anything that is not one of the six page recipes,
use the same tokens and rules: the reading scale, the spacing steps, the color roles, flat
surfaces with `rule` hairlines, Stroke icons and the accent budget. Reuse a component's
markup and classes from DESIGN.md wherever one fits instead of inventing a new one.

## Check your work

- The page follows its recipe's component order, and every component's markup matches DESIGN.md.
- No value outside the tokens, no Tailwind default palette or scale.
- The accent appears at most twice; no shadow, gradient or emoji.
- Icons come from `@hugocxl/icons` (Stroke) and figures from `@hugocxl/vectors`.
- The page works at 320, 760, 761 and 1440 px in light and dark.

Reference page: https://hugocxl.github.io/design-system/
