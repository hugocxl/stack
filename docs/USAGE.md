# Use IconsCXL

Bring the same rounded icon family to your website, app, or design. Choose your platform below.

## Choose an integration

| Need | Start here |
| --- | --- |
| Use an SVG in a web page, design, or native app | [Raw SVGs](#raw-svgs) |
| Use icons in SwiftUI, UIKit, or AppKit | [Swift / SwiftUI](#swift--swiftui) |
| Use SVG strings in JavaScript or on the server | [JavaScript](#javascript-no-framework) |
| Use icons in a React app | [React](#react) |
| Use icons in React Native or Expo | [React Native / Expo](#react-native--expo) |

All integrations use the same icon names and source artwork. The default icon
size is 16, and icons use `currentColor` or an explicit platform tint.

## Raw SVGs

Download or clone the repository and copy the SVGs you need from [`icons/`](../icons/).
No dependencies or build step are required to use the artwork.

```sh
git clone https://github.com/hugocxl/iconscxl.git
```

Icons use `currentColor` and filled vector geometry. New UI symbols use a
16 × 16 canvas; preserve the viewBox and aspect ratio when sizing legacy assets.
The default uses duotone only for meaningful surfaces or depth. Linear symbols
such as arrows and chevrons use one opaque tint; Pencil and Trash retain their
secondary body fill. Existing default and `/duotone` imports select this treatment.
Solid and Stroke artwork lives in `icons/styles/solid` and `icons/styles/stroke`.

Inline an SVG in HTML to inherit CSS `color`. When loading SVGs through an
`<img>` tag, parent CSS color does not propagate into the file. Native apps can
load them as template images and apply their own tint.

Open [`index.html`](../index.html) locally for a searchable, offline gallery with
category/style filters, tint and size controls, SVG copying, and downloads.
Browse the [complete catalog](../docs/CATALOG.md) for every available name.

## Swift / SwiftUI

The Swift package exposes the `IconsCXL` library for Swift 6+, macOS 12+, iOS
15+, tvOS 15+, and watchOS 8+. Add the repository as a Swift Package Manager
dependency using a release tag, or add it as a local package while developing.
Then add `IconsCXL` to your app target. For a `Package.swift` dependency:

```swift
.package(url: "https://github.com/hugocxl/iconscxl.git", from: "0.1.9")
```

Add `.product(name: "IconsCXL", package: "iconscxl")` to your target's dependencies.

```swift
import IconsCXL
import SwiftUI

Icon.search.image
    .resizable()
    .scaledToFit()
    .frame(width: 24, height: 24)
    .foregroundStyle(.secondary)
    .accessibilityLabel("Search")
```

Use `Icon.search.uiImage` in UIKit or `Icon.search.nsImage` in AppKit.
Images come from the package's vector asset catalog and use template rendering.
`Icon.allCases` and `Icon(rawValue: "search")` support dynamic selection.

## JavaScript (no framework)

All JavaScript integrations come from one npm package, `@hugocxl/iconscxl`.
Choose `/js`, `/react`, or `/react-native`; per-icon imports are available too.
React and React Native dependencies are optional, so a plain JavaScript install
adds no framework dependencies.

```sh
npm install @hugocxl/iconscxl
```

```js
import { SearchIcon } from '@hugocxl/iconscxl/js';
// Or: import { SearchIcon } from '@hugocxl/iconscxl/js/search';
// The package root also exports the plain JavaScript adapter.
document.querySelector('#search-icon').innerHTML = SearchIcon;
```

The JS adapter exports SVG strings, usable in the browser or server-side.
These are the trusted, bundled artwork strings. Use CSS to size and tint inline
SVGs (`#search-icon svg { width: 24px; height: 24px; color: rebeccapurple; }`).
Add accessible labels on the containing control when used as button icons.

## React

The React package provides typed ESM components with per-icon exports and tree
shaking. Install it from npm:

```sh
npm install @hugocxl/iconscxl
```

```tsx
import { SearchIcon } from '@hugocxl/iconscxl/react';
// Per-icon imports are also supported:
import { TerminalIcon } from '@hugocxl/iconscxl/react/terminal';

<SearchIcon size={24} color="currentColor" aria-label="Search" />
<TerminalIcon size={16} />
```

Components support React 18 and 19, SVG props, and forwarded SVG refs.
Unlabelled icons are decorative (`aria-hidden`). Supply `aria-label` or
`aria-labelledby` for meaningful icons; explicit `aria-hidden` takes precedence.
For icon-only buttons, label the button and leave the icon decorative.

## React Native / Expo

The React Native package provides the same typed, per-icon API for React Native
and Expo. Install it from npm along with its peer dependency:

```sh
npm install @hugocxl/iconscxl
npx expo install react-native-svg
# Or, in a bare React Native app:
npm install react-native-svg
```

```tsx
import { SearchIcon } from '@hugocxl/iconscxl/react-native';

<SearchIcon size={24} color="#64748b" accessibilityLabel="Search" />
```

Native components accept `react-native-svg` props and refs. No SVG transformer
or custom Metro configuration is needed. Install iOS pods using your app's
normal workflow.

Both framework adapters ship typed ESM with per-icon exports and tree shaking.
The peer ranges are compatibility declarations; CI checks the versions in the
lockfile, not every older React Native release.

## Choose a drawing style

Rounded Duotone remains the default, including all 81 retained brand marks.
The 2,117 original UI icons also support Rounded Solid and Rounded Stroke.
Brands are intentionally absent from those two style namespaces.

```tsx
import { SearchIcon } from '@hugocxl/iconscxl/react'; // Duotone
import { SearchIcon as SolidSearchIcon } from '@hugocxl/iconscxl/react/solid';
import { SearchIcon as StrokeSearchIcon } from '@hugocxl/iconscxl/react/stroke/search';
```

The same style paths work under `/js` and `/react-native`. Explicit `/duotone`
and `/duotone/search` imports are aliases of the default artwork. Use
`@hugocxl/iconscxl/catalog.json` to inspect names, categories, keywords, provenance,
supported styles, and `defaultTone` (`monochrome` or `duotone`).
Style namespaces remain tree-shakeable.

```swift
Icon.search.image         // Rounded Duotone
SolidIcon.search.image    // Rounded Solid
StrokeIcon.search.image   // Rounded Stroke
```

All three Swift enums expose `allCases`, `rawValue`, `image`, `uiImage` (UIKit),
and `nsImage` (AppKit). Existing names and imports remain available; the UI artwork
has been redrawn, including historical `*-fill` names, so upgrading changes their
appearance. This release does not include Hugeicons or SF Symbols artwork.

