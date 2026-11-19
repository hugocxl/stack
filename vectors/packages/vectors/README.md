# @hugocxl/vectors

**2,000 isometric line illustrations for websites and apps**, with typed,
tree-shakeable exports for JavaScript, React, React Native and Expo.

```sh
npm install @hugocxl/vectors
```

```js
// Pure JavaScript: SVG strings, no framework dependency.
import { ModularDesignVector } from '@hugocxl/vectors/js';
// React components:
import { ModularDesignVector as ModularDesign } from '@hugocxl/vectors/react';
// React Native components (install react-native-svg in your app):
import { ModularDesignVector as NativeModularDesign } from '@hugocxl/vectors/react-native';
// Per-vector imports:
import { FastPerformanceVector } from '@hugocxl/vectors/react/fast-performance';
```

Components draw in `currentColor` and accept `size` (the width; the height
follows at 4:3), `color`, platform SVG props and refs. Each keeps the
illustration's title and description for assistive technology.
`@hugocxl/vectors/catalog.json` lists every name with its category and use case.

[Browse the vectors](https://hugocxl.github.io/stack/vectors/browse.html) ·
[Read the guide](https://hugocxl.github.io/stack/vectors/docs.html) ·
[Source](https://github.com/hugocxl/stack/tree/main/vectors)

AI agents: the package ships a skill in `skills/vectors/` with the rules and a search by
meaning (`node node_modules/@hugocxl/vectors/skills/vectors/scripts/search.mjs empty inbox`).

MIT licensed.
