# Component recipes

One JSON file per component. A recipe is platform-neutral: it says what the component is for,
its anatomy, its options, its states, the design-system tokens it uses and the rules every
implementation keeps. Each implementation (React, Swift, later React Native) builds the recipe
with the names listed under `platforms`; `null` means the component does not exist on that
platform.

`scripts/check-recipes.mjs` fails when a recipe names an export or a Swift type that does not
exist, when an implementation ships a component without a recipe, or when the website has no
example for a recipe.
