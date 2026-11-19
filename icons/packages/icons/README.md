# @hugocxl/icons

**2,462 rounded icons for apps, websites, and developer tools**, with typed,
tree-shakeable exports for JavaScript, React, React Native, and Expo.

Choose Duotone, Solid, or Stroke for 2,381 UI icons, plus 81 brand marks in the
default style: 7,224 SVG drawings in total. SwiftUI, UIKit, and AppKit are also
supported through the [Swift package](https://hugocxl.github.io/icons/docs.html).

```sh
npm install @hugocxl/icons
```

```js
// Pure JavaScript: SVG strings, no framework dependency.
import { SearchIcon } from '@hugocxl/icons/js';
// React components:
import { SearchIcon as ReactSearchIcon } from '@hugocxl/icons/react';
// React Native components (install react-native-svg in your app):
import { SearchIcon as NativeSearchIcon } from '@hugocxl/icons/react-native';
// Per-icon imports:
import { SearchIcon as singleSvg } from '@hugocxl/icons/js/search';
```

React adapters accept `size`, `color`, platform SVG props, and refs. Unlabelled
web icons are decorative; use `aria-label` for meaningful icons. Native apps
should install `react-native-svg` (Expo: `npx expo install react-native-svg`).
The package root is the pure JavaScript adapter. Framework peers are optional;
install the peers needed by the adapter you use.

[Browse the complete catalog](https://github.com/hugocxl/icons/blob/main/docs/CATALOG.md)
or read the [full integration guide](https://hugocxl.github.io/icons/docs.html).
Redistribute LICENSE, NOTICE and THIRD_PARTY_LICENSES.md with the artwork.

Style imports use `/js/solid`, `/react/solid`, `/react-native/solid` or the
matching `/stroke` paths. Per-icon style imports are supported too, for example
`@hugocxl/icons/react/stroke/search`. `/duotone` explicitly selects the default.
Brand marks are available in Duotone only. The exported `catalog.json` records
style availability, category, keywords, provenance, and `defaultTone` for every
name. Arrows, chevrons and other linear symbols are fully opaque; two tones are
reserved for meaningful surfaces and depth, such as the Pencil and Trash bodies.

Use an assigned color for a language, tool, file type or brand by passing
`color={defaultColor('folder')}` to its component. Import `defaultColor` from
`@hugocxl/icons/colors`. The web value follows the design-system hue token or
CSS color scheme. Pass `'light'` or `'dark'` as the second argument for a native
hex value. The catalog’s optional `defaultColor` field names the hue.

AI agents: the package ships a skill in `skills/icons/` with the rules and a catalog
search (`node node_modules/@hugocxl/icons/skills/icons/scripts/search.mjs trash`).
