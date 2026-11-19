---
name: icons
description: Use @hugocxl/icons for every icon in a web, React, React Native or Swift interface. Covers finding the right icon name, importing it on each platform, choosing a style, sizing, coloring and labelling it. Use it whenever you add, change or review an icon, or are tempted to reach for another icon set, an emoji or a symbol character.
---

# @hugocxl/icons

A family of rounded icons in three styles (Duotone, Solid, Stroke) on a 16 × 16 grid,
with the same names for SVG files, JavaScript, React, React Native and Swift.

## Rules

1. **Only these icons.** Never use another icon library (Lucide, Heroicons, Font Awesome,
   Material, Phosphor, Tabler, react-icons…), an emoji or a symbol character such as `→`,
   `✓` or `◐` as an icon.
2. **Never guess a name.** Look it up with the search script below, and check the names you
   are about to use before you finish. A made-up name fails at import time.
3. **Icons label actions.** Put an icon before the words of a link, button or label, or alone
   in an icon button that has an accessible label. Do not decorate headings or body text.
4. **One style per surface.** With `@hugocxl/design-system`, use **Stroke**. Elsewhere,
   pick one style for the product and keep it. Brand marks exist in Duotone only.
5. **Icons take the text color.** They draw in `currentColor`. Color an icon only when the
   color means something: an assigned kind color or a status (see below).

## Find an icon

Search the catalog of the installed version. The script ships next to this file:

```sh
node <this skill's directory>/scripts/search.mjs trash
node <this skill's directory>/scripts/search.mjs "arrow right" --style stroke --limit 5
node <this skill's directory>/scripts/search.mjs --check search settings trash   # exit 1 if any name is missing
```

It prints each match's name, export, styles, category and assigned color. Add `--json` for
machine-readable output. In a project, the script reads
`node_modules/@hugocxl/icons/catalog.json`; otherwise it reads the catalog bundled with this
skill. The [icon browser](https://hugocxl.github.io/stack/icons/browse.html) shows the same set.

Names are kebab-case (`arrow-up-right`, `circle-check`). The export is the name in PascalCase
with an `Icon` suffix: `arrow-up-right` → `ArrowUpRightIcon`.

## Use an icon

```sh
npm install @hugocxl/icons
```

| Platform | Import |
| --- | --- |
| React | `import { SearchIcon } from '@hugocxl/icons/react/stroke'` |
| React, one icon | `import { SearchIcon } from '@hugocxl/icons/react/stroke/search'` |
| React Native / Expo | `import { SearchIcon } from '@hugocxl/icons/react-native/stroke'` (needs `react-native-svg`) |
| JavaScript (SVG string) | `import { SearchIcon } from '@hugocxl/icons/js/stroke'` |
| Catalog | `import catalog from '@hugocxl/icons/catalog.json' with { type: 'json' }` |

The style segment is `/stroke`, `/solid` or `/duotone`. Leaving it out selects Duotone, the
default. Every path also works without the style (`@hugocxl/icons/react/search`).

```tsx
import { BookOpenIcon, SearchIcon } from '@hugocxl/icons/react/stroke';

<button type="button" aria-label="Search"><SearchIcon size={16} /></button>
<a href="/docs"><BookOpenIcon />Read the guide</a>
```

- React and React Native components take `size` (default `16`), `color` (default
  `currentColor`), every SVG prop and a ref.
- Web components are decorative (`aria-hidden`) unless they get `aria-label` or
  `aria-labelledby`. For an icon-only button, label the **button** and leave the icon
  decorative. In React Native, pass `accessibilityLabel`.
- JavaScript exports are trusted SVG strings: inline them with `innerHTML` and size and tint
  them with CSS (`svg { width: 1em; height: 1em; color: inherit }`). An SVG loaded through
  `<img>` cannot inherit the text color.
- Keep icons at 16, 20 or 24 px; they are drawn for 16. For an illustration larger than about
  64 px, use `@hugocxl/vectors` instead.

With `@hugocxl/design-system` markup, give the inline SVG `class="ds-icon"` and
`data-icon="<name>"`, or pass `className="ds-icon"` to the React component. It then sizes to
`1em` and keeps the system's spacing.

### Swift

```swift
.package(url: "https://github.com/hugocxl/stack.git", from: "0.1.0")   // the hugocxlStack package
// target dependency: .product(name: "Icons", package: "stack")

import Icons
StrokeIcon.search.image.resizable().frame(width: 16, height: 16)
```

`Icon` is Duotone, `SolidIcon` and `StrokeIcon` are the other styles. Each case is the name in
camelCase and has `image`, `uiImage` and `nsImage`.

## Color

- **Default.** Inherit the surrounding text color. Action icons (links, buttons, icon
  buttons) are never colored.
- **Kind.** A language, tool, file type or brand can take the hue the library assigns, so the
  same thing has the same color everywhere. Use it for items in lists, trees and tables only.

  ```tsx
  import { FolderIcon } from '@hugocxl/icons/react/stroke';
  import { defaultColor } from '@hugocxl/icons/colors';

  <FolderIcon color={defaultColor('folder')} />
  ```

  `defaultColor(name)` returns a CSS color that uses the design system's `--ds-<hue>` token
  when present, or `undefined` when the icon has no assigned hue. Pass `'light'` or `'dark'`
  as the second argument for a hex value in React Native. In design-system markup, use
  `data-color="<hue>"` with the hue from the catalog's `defaultColor` field.
- **Status.** Before the words that name a state: `circle-check` for success,
  `triangle-alert` for warning, `circle-x` for error, `circle-info` for info. In
  design-system markup, add `data-status="success|warning|error|info"`.

The words beside a colored icon always say what it means; color alone never does.

## Check your work

- Every icon name came from the search script, and `--check` passes for all of them.
- No other icon package is imported and no emoji or symbol character stands in for an icon.
- One style per surface (Stroke with the design system).
- Every icon-only control has an accessible label.

Full documentation: https://hugocxl.github.io/stack/icons/docs.html
