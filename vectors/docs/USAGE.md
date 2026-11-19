# Use @hugocxl/vectors

@hugocxl/vectors is a library of 2,000 isometric line illustrations for websites and apps.
Every platform uses the same names and the same artwork. Pick yours below.

## Choose an integration

| Need | Start here |
| --- | --- |
| Drop an illustration into a page, a design file or a native app | [SVG files](#svg-files) |
| Use SVG strings in JavaScript or on the server | [JavaScript](#javascript) |
| Use illustrations in a React app | [React](#react) |
| Use illustrations in React Native or Expo | [React Native](#react-native) |
| Use illustrations in SwiftUI, UIKit or AppKit | [Swift](#swift) |

Every illustration is drawn on a transparent 480 × 360 canvas (4:3) and has a
stable kebab-case name, such as `modular-design`. Each SVG carries a `<title>`
and a `<desc>`. Use the [browser](https://hugocxl.github.io/stack/vectors/browse.html)
to search by name, category or use case.

## Install

All JavaScript integrations come from one npm package. React, React Native and
`react-native-svg` are optional peer dependencies, so a plain JavaScript install
adds no framework.

```sh
npm install @hugocxl/vectors
```

| Import path | Exports |
| --- | --- |
| `@hugocxl/vectors` or `@hugocxl/vectors/js` | SVG strings |
| `@hugocxl/vectors/js/<name>` | One SVG string |
| `@hugocxl/vectors/react` | React components |
| `@hugocxl/vectors/react/<name>` | One React component |
| `@hugocxl/vectors/react-native` | React Native components |
| `@hugocxl/vectors/react-native/<name>` | One React Native component |
| `@hugocxl/vectors/catalog.json` | Names, titles, descriptions, categories and use cases |

Export names are the file name in PascalCase with a `Vector` suffix:
`modular-design.svg` is `ModularDesignVector` on every JavaScript platform.
The package is ESM with one module per illustration and `sideEffects: false`, so
bundlers keep only the illustrations you import. Per-illustration paths keep
development servers fast too.

## SVG files

Every illustration is a standalone file in
[`figures/`](https://github.com/hugocxl/stack/tree/main/vectors/figures). Download one
from the browser, or clone the repository. No build step is needed.

```sh
git clone https://github.com/hugocxl/stack.git   # the figures are in stack/vectors/figures
```

```html
<img src="/images/modular-design.svg"
     alt="Four independent modules fit into one assembly"
     width="480" height="360">
```

A file loaded with `<img>` draws in its own neutral grey (`#8792a2`), which reads
on light and dark backgrounds. To follow your page colors, inline the SVG instead;
see [Recoloring](#recoloring).

## JavaScript

The JavaScript adapter exports each illustration as an SVG string, byte for byte
the file in `figures/`. Use it in the browser or on the server.

```js
import { ModularDesignVector } from '@hugocxl/vectors/js';
// Or import a single illustration:
// import { ModularDesignVector } from '@hugocxl/vectors/js/modular-design';

document.querySelector('#hero-art').innerHTML = ModularDesignVector;
```

```css
#hero-art svg { width: 100%; height: auto; color: currentColor; }
```

The strings are the trusted artwork bundled with the package, so inserting them
with `innerHTML` is safe.

## React

React components are typed, forward their ref to the `<svg>` element and accept
every SVG prop. They support React 18 and 19.

```tsx
import { ModularDesignVector } from '@hugocxl/vectors/react';
import { FastPerformanceVector } from '@hugocxl/vectors/react/fast-performance';

<ModularDesignVector />
<FastPerformanceVector size={320} color="#64748b" className="hero-art" />
```

| Prop | Default | Effect |
| --- | --- | --- |
| `size` | `480` | Width in pixels. The height is set to `size × 3 / 4`. |
| `color` | `"currentColor"` | Line color. The default follows the surrounding text color. |
| `width`, `height` | from `size` | Override one dimension. |
| `ref` | | The `<svg>` element. |

## React Native

React Native components use `react-native-svg` and take the same `size` and
`color` props. They work in Expo and bare React Native apps without an SVG
transformer or Metro configuration.

```sh
npm install @hugocxl/vectors
npx expo install react-native-svg
# Or, in a bare React Native app:
npm install react-native-svg
```

```tsx
import { ModularDesignVector } from '@hugocxl/vectors/react-native';

<ModularDesignVector size={280} color="#64748b" />
```

Components accept `react-native-svg` props and refs. Each one is an accessible
image labelled with the illustration title. Pass `accessibilityLabel` to change
the label or `accessible={false}` when it is decorative.

## Swift

The Swift package exposes the `Vectors` library for Swift 6, macOS 12, iOS 15,
tvOS 15 and watchOS 8 or later. It ships in the `hugocxlStack` package at the root
of the [stack](https://github.com/hugocxl/stack) monorepo, together with `Icons`. Add the
repository with Swift Package Manager, using a release tag:

```swift
.package(url: "https://github.com/hugocxl/stack.git", from: "0.1.0")
```

Then add `.product(name: "Vectors", package: "stack")` to your target. The
`Vector` enum has one case per illustration, named in camelCase.

```swift
import SwiftUI
import Vectors

Vector.modularDesign.image
    .resizable()
    .aspectRatio(4 / 3, contentMode: .fit)
    .frame(maxWidth: 320)
    .foregroundStyle(.secondary)
    .accessibilityLabel("Four independent modules fit into one assembly")
```

In UIKit, use `Vector.modularDesign.uiImage` in a `UIImageView` and set its
`tintColor`. In AppKit, use `Vector.modularDesign.nsImage` and
`contentTintColor`. Images come from a vector asset catalog that preserves the
vector data and uses template rendering, so they scale cleanly and take your
tint. `Vector.allCases` and `Vector(rawValue: "modular-design")` support dynamic
selection.

## Recoloring

Each illustration draws with `stroke="currentColor"` and up to four levels
of opacity: highlights, contours and two quieter construction lines.
Recoloring changes one color and keeps that hierarchy.

| Platform | How to recolor |
| --- | --- |
| Inline SVG | Set CSS `color` on the `<svg>` or remove its `color` attribute to inherit. |
| `<img>` | Not possible; the file keeps its neutral grey. Inline it instead. |
| React and React Native | The `color` prop. The default is `currentColor`. |
| Swift | `foregroundStyle`, `tintColor` or `contentTintColor`. |

The backgrounds are transparent, so the page shows through every gap. Use one
color per illustration; the artwork is not designed for gradients or fills.

## Sizing

The canvas is 480 × 360 points and every line uses a non-scaling stroke, so the
lines stay crisp and thin at any size. Keep the 4:3 aspect ratio.

- On the web, set a width and let the height follow:
  `style={{ width: '100%', height: 'auto' }}` in React, or
  `svg { width: 100%; height: auto; }` in CSS.
- In React and React Native, `size` sets the width and derives the height.
- In SwiftUI, use `.resizable()` with `.aspectRatio(4 / 3, contentMode: .fit)`.

The illustrations read well from about 160 points wide. Below that, prefer an
icon from [@hugocxl/icons](https://hugocxl.github.io/stack/icons/).

## Accessibility

Every SVG has `role="img"`, a `<title>` that names it and a `<desc>` that
describes the scene. The web components render both, so screen readers announce
the illustration without extra work.

- If the illustration repeats nearby text, hide it: `aria-hidden={true}` in
  React, `alt=""` on an `<img>`, `accessible={false}` in React Native or
  `.accessibilityHidden(true)` in SwiftUI.
- To describe it in your own words, pass `aria-label` (web) or
  `accessibilityLabel` (React Native and Swift).
- Line colors are yours to choose. Check that the contours keep at least a 3:1
  contrast with the background.

## Catalog

`@hugocxl/vectors/catalog.json` lists every illustration with its `name`,
`export`, `title`, `description`, `category`, `categoryId`, `placement` (where it
fits on a site), `priority` and `file`. Use it to build pickers or search.

```js
import catalog from '@hugocxl/vectors/catalog.json' with { type: 'json' };

const empty = catalog.filter(item => item.categoryId === 'feedback-and-empty-states');
```

## License

The artwork and code are [MIT licensed](https://github.com/hugocxl/stack/blob/main/vectors/LICENSE).
Use them in personal and commercial work and keep the license notice with copies of
the source. The drawing style draws on the visual rules in
[Hairline by Lucas Marques](https://hairline.lucasmarkes.com/skills).
