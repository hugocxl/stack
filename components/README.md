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

### Product interfaces

Desktop tools set the compact density at the root: 13pt reading and 28pt targets, with every
token and rule unchanged. Panes, toolbars, property rows, disclosures, menus, search fields,
empty states and data marks build the workspace; `.dsSounds(true)` lets the components play
@hugocxl/sounds.

```swift
WindowContent()
    .dsTheme()
    .dsDensity(.compact)
    .dsSounds(settings.sounds)

DSPane("Inspector", icon: StrokeIcon.sliders) {
    DSPropertyRow("Opacity") {
        DSSlider(value: $opacity, in: 0...100, ticks: 0, defaultValue: 100, editable: true,
                 onEditingChanged: { editing in if !editing { commitUndo() } })
    }
}
```

## Recipes

`@hugocxl/components/recipes.json` lists every recipe: what it is for, its anatomy, options,
states, tokens, rules and accessibility.

## License

[MIT](LICENSE). Made by [Hugo](https://github.com/hugocxl).
