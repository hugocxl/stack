# IconsCXL

**2,233 rounded icons for apps, websites, and developer tools**, with typed,
tree-shakeable exports for JavaScript, React, React Native, and Expo.

Choose Duotone, Solid, or Stroke for 2,152 UI icons, plus 81 brand marks in the
default style: 6,432 SVG drawings in total. SwiftUI, UIKit, and AppKit are also
supported through the [Swift package](https://github.com/hugocxl/iconscxl#swift--swiftui).

```sh
npm install @hugocxl/iconscxl
```

```js
// Pure JavaScript: SVG strings, no framework dependency.
import { SearchIcon } from '@hugocxl/iconscxl/js';
// React components:
import { SearchIcon as ReactSearchIcon } from '@hugocxl/iconscxl/react';
// React Native components (install react-native-svg in your app):
import { SearchIcon as NativeSearchIcon } from '@hugocxl/iconscxl/react-native';
// Per-icon imports:
import { SearchIcon as singleSvg } from '@hugocxl/iconscxl/js/search';
```

React adapters accept `size`, `color`, platform SVG props, and refs. Unlabelled
web icons are decorative; use `aria-label` for meaningful icons. Native apps
should install `react-native-svg` (Expo: `npx expo install react-native-svg`).
The package root is the pure JavaScript adapter. Framework peers are optional;
install the peers needed by the adapter you use.

[Browse the complete catalog](https://github.com/hugocxl/iconscxl/blob/main/docs/CATALOG.md)
or read the [full integration guide](https://github.com/hugocxl/iconscxl#readme).
Redistribute LICENSE, NOTICE and THIRD_PARTY_LICENSES.md with the artwork.

Style imports use `/js/solid`, `/react/solid`, `/react-native/solid` or the
matching `/stroke` paths. Per-icon style imports are supported too, for example
`@hugocxl/iconscxl/react/stroke/search`. `/duotone` explicitly selects the default.
Brand marks are available in Duotone only. The exported `catalog.json` records
style availability, category, keywords, provenance, and `defaultTone` for every
name. Arrows, chevrons and other linear symbols are fully opaque; two tones are
reserved for meaningful surfaces and depth, such as the Pencil and Trash bodies.
