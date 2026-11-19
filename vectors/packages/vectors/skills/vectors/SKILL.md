---
name: vectors
description: Use @hugocxl/vectors for every illustration in a web, React, React Native or Swift interface, such as heroes, feature sections, onboarding, empty states, errors and docs. Covers finding the vector that means what the page says, importing it on each platform, sizing, coloring and labelling it. Use it whenever a page needs a picture, figure or illustration, or you are tempted to use stock art, an emoji or another illustration set.
---

# @hugocxl/vectors

2,000 isometric line illustrations on a transparent 480 × 360 (4:3) canvas. Each one shows a
specific moment on a website or in a product, such as a launch, an empty inbox or a failed
payment, and has the same name in SVG files, JavaScript, React, React Native and Swift.

## Rules

1. **Only these illustrations.** Never use stock photography, another illustration set,
   generated images, emoji or clip art. A screenshot of the product itself is the only other
   image a page may show.
2. **Choose by meaning.** Search for what the section says, then read the match's
   description and make sure the drawing says the same thing. Never pick a vector for its
   look alone, and never guess a name.
3. **One idea per figure.** Use a vector where it explains something: a hero, a feature, a
   step, a state. Do not use it as decoration or as a background.
4. **Keep its shape and line.** Never crop, stretch, rotate, fill or recolor parts of a
   vector, and never put it on a pattern or photo. Keep the 4:3 ratio.
5. **One color.** A vector draws in `currentColor`. Give it the text color; never the brand
   accent, a gradient or several colors.

## Find a vector

Search the catalog of the installed version. The script ships next to this file:

```sh
node <this skill's directory>/scripts/search.mjs empty inbox
node <this skill's directory>/scripts/search.mjs "payment failed" --limit 5
node <this skill's directory>/scripts/search.mjs --categories
node <this skill's directory>/scripts/search.mjs "launch" --category landing-and-marketing
node <this skill's directory>/scripts/search.mjs --check product-launch empty-inbox   # exit 1 if any name is missing
```

Each match shows its name, export, title, where it fits on a site and what it draws. Add
`--json` for machine-readable output. In a project, the script reads
`node_modules/@hugocxl/vectors/catalog.json`; otherwise it reads the catalog bundled with this
skill. The [vectors browser](https://hugocxl.github.io/stack/vectors/browse.html) shows the same
set by use case.

Names are kebab-case (`modular-design`). The export is the name in PascalCase with a `Vector`
suffix: `modular-design` → `ModularDesignVector`.

Related states share an object and differ by a badge (check for done, x for failed, clock for
pending). When a page shows several states of one thing, use the matching siblings, such as
`payment-failed` and `payment-methods`.

## Use a vector

```sh
npm install @hugocxl/vectors
```

| Platform | Import |
| --- | --- |
| React | `import { ModularDesignVector } from '@hugocxl/vectors/react/modular-design'` |
| React Native / Expo | `import { ModularDesignVector } from '@hugocxl/vectors/react-native/modular-design'` (needs `react-native-svg`) |
| JavaScript (SVG string) | `import { ModularDesignVector } from '@hugocxl/vectors/js/modular-design'` |
| Catalog | `import catalog from '@hugocxl/vectors/catalog.json' with { type: 'json' }` |

Prefer the per-vector path shown above; the package index (`@hugocxl/vectors/react`) works
too but makes development servers parse every vector.

```tsx
import { EmptyInboxVector } from '@hugocxl/vectors/react/empty-inbox';

<EmptyInboxVector style={{ width: '100%', maxWidth: 320, height: 'auto' }} />
```

- React and React Native components take `size` (the width, default `480`; the height
  follows at 3:4), `color` (default `currentColor`), every SVG prop and a ref.
- On the web, size by width and let the height follow: `width: 100%; height: auto`.
- Vectors read well from about 160 px wide. Below that, use an icon from `@hugocxl/icons`.
- JavaScript exports are trusted SVG strings: inline them with `innerHTML`. An SVG loaded
  with `<img>` cannot follow the text color and draws in a neutral grey.

With `@hugocxl/design-system` markup, put the vector in a `figure-wide` or `figure-grid`
component: inline the SVG inside `.ds-media`, replace its root `xmlns` attribute with
`class="ds-vector"` and `data-vector="<name>"`, remove its `color` attribute, and name it in
the caption. In React, pass `className="ds-vector"`.

### Swift

```swift
.package(url: "https://github.com/hugocxl/stack.git", from: "0.1.0")   // the hugocxlStack package
// target dependency: .product(name: "Vectors", package: "stack")

import Vectors
Vector.emptyInbox.image
    .resizable()
    .aspectRatio(4 / 3, contentMode: .fit)
    .foregroundStyle(.secondary)
```

`Vector` has one case per name in camelCase, with `image`, `uiImage` and `nsImage`.

## Accessibility

Every SVG has `role="img"`, a `<title>` and a `<desc>`, and the components render them.

- Keep the `title` and `desc` when you inline a vector; they are its accessible name.
- If the vector repeats nearby text, hide it: `aria-hidden` in React, `alt=""` on an
  `<img>`, `accessible={false}` in React Native, `.accessibilityHidden(true)` in SwiftUI.
- To describe it in your own words, pass `aria-label` or `accessibilityLabel`.
- Keep the lines at 3:1 contrast or more against the background.

## Check your work

- Every vector name came from the search script, its description matches the section, and
  `--check` passes for all of them.
- No stock art, emoji, other illustration set or generated image is on the page.
- Vectors keep their 4:3 ratio, one color and their accessible name.

Full documentation: https://hugocxl.github.io/stack/vectors/docs.html
