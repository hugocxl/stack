# @hugocxl/components

### The design system, as components.

Buttons, fields, feedback, content and the page itself, built on
[@hugocxl/design-system](https://hugocxl.github.io/stack/design-system/) tokens. Every
component starts as a platform-neutral recipe, and React and SwiftUI build the same one.

[See every component](https://hugocxl.github.io/stack/components/)

## React

```sh
pnpm add @hugocxl/components
```

```tsx
import "@hugocxl/components/styles.css"; // Geist, the tokens and the components
import { Button, TextField, Notice } from "@hugocxl/components/react";
import { ArrowRightIcon } from "@hugocxl/icons/react/arrow-right";

<Button icon={<ArrowRightIcon />}>Get started</Button>
```

## Swift

Add `https://github.com/hugocxl/stack` with Swift Package Manager and use the `Components`
library:

```swift
import Components

DSPage {
    DSTitle("Settings", byline: "Fieldwork")
    DSSwitch("Sounds", isOn: $sounds)
    DSButton("Save changes") { save() }
}
```

## Recipes

`@hugocxl/components/recipes.json` lists every recipe: what it is for, its anatomy, options,
states, tokens, rules and accessibility.

## License

[MIT](LICENSE). Made by [Hugo](https://github.com/hugocxl).
