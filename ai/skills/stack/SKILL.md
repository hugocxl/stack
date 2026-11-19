---
name: stack
description: The @hugocxl stack — @hugocxl/design-system, @hugocxl/icons, @hugocxl/vectors and @hugocxl/sounds — used together. Read it first for any interface work in a project that uses the stack, when starting a new @hugocxl project, or when deciding between an icon and an illustration, choosing which library covers a need, or checking that a change follows the stack.
---

# The @hugocxl stack

Four libraries, designed to work as one. Every @hugocxl project builds its interface from them
and from nothing else, so any agent working on any project produces the same result.

| Need | Library | Skill |
| --- | --- | --- |
| Type, color, spacing, layout, pages, components | `@hugocxl/design-system` | `design-system` |
| A symbol that labels an action or a kind of thing | `@hugocxl/icons` | `icons` |
| An illustration that explains an idea or a state | `@hugocxl/vectors` | `vectors` |
| Sound or haptic feedback for a direct action | `@hugocxl/sounds` | `sounds` |

Read this skill first, then the skill of each library the task touches. Each library's skill
ships inside its npm package, so it always matches the installed version.

## Rules

1. **Nothing from outside the stack.** No other icon set, illustration, stock image, emoji used
   as an icon, UI kit, theme, color palette, font or interface sound library. If the stack has
   no answer, say so and ask; do not improvise one.
2. **The design system decides how things look.** Use its tokens for every color, size, space,
   radius and font, and its components and recipes for pages. See the `design-system` skill.
3. **Never guess a name.** Find icon and vector names with the search scripts in their skills,
   and check every name before you finish.
4. **Meaning first.** An icon labels an action, a vector explains an idea, a sound confirms what
   the hand did. None of them is decoration.
5. **Check before you finish.** Run `npx @hugocxl/ai check` and fix every error.

## Icon or vector?

- **Icon** (`@hugocxl/icons`): 16–24 px, inline with words or alone in an icon button; it names
  an action (`search`, `trash`) or a kind (`folder`, `terminal`). Stroke style with the design
  system.
- **Vector** (`@hugocxl/vectors`): 160 px wide or more, in a figure; it shows a whole idea or
  state (`empty-inbox`, `payment-failed`). Pick it by what the section says.
- Between 24 and 160 px, choose by role, not size: a label is an icon, an explanation is a
  vector. Never scale an icon up into an illustration or a vector down into an icon.

## How the libraries fit together

- **Color.** Icons and vectors draw in `currentColor`, so they follow the design system's `ink`
  and `muted` in both themes. Only icons may take a color: a kind hue
  (`defaultColor('folder')` from `@hugocxl/icons/colors` resolves to the design system's
  `--ds-yellow`) or a status role. Never the accent.
- **Markup.** In design-system pages, icons carry `class="ds-icon"` and vectors
  `class="ds-vector"`, inside the components DESIGN.md defines.
- **Sound.** Pair each control with its sound from the `sounds` skill:

  | Design-system element | Sound |
  | --- | --- |
  | `button` (the one filled button) | `down-primary` on press, `up` on release |
  | Other buttons and icon buttons | `down`, then `up` |
  | Theme switch and other toggles | `latch-down` on, `latch-up` off |
  | Pager, tabs, segmented controls | `tick` |
  | Menu, popover or dialog opening | `open` |
  | `form` result | `success`, `warning` or `error` when the result is known |

  Links that navigate make no sound. Sounds are optional: give people a setting to turn them off.

## Start a new project

```sh
npm install @hugocxl/design-system @hugocxl/icons @hugocxl/vectors @hugocxl/sounds
npx @hugocxl/ai init
```

`init` writes the stack's section into `AGENTS.md`, points `CLAUDE.md` at it, and copies the
skills of the installed libraries into `.agents/skills/` and `.claude/skills/`. Run
`npx @hugocxl/ai sync` after upgrading any library, and commit the result.

Then choose the integration the project needs:

- **Static site:** serve the design system's `system/` folder and copy component markup from
  DESIGN.md; inline icon and vector SVGs from their JavaScript exports.
- **React (Next.js, Vite, Astro):** Tailwind v4 with `@import "@hugocxl/design-system/tailwind";`,
  icons from `@hugocxl/icons/react/stroke`, vectors from `@hugocxl/vectors/react/<name>`.
- **React Native / Expo:** tokens from `@hugocxl/design-system/tokens`, icons and vectors from
  their `/react-native` paths with `react-native-svg`. Sounds are web only.
- **Swift:** the `Icons` and `Vectors` Swift packages and the token values from
  `@hugocxl/design-system/tokens.json`.

## Work on a task

1. Read the skill of each library the task touches.
2. Plan the page or screen: the recipe, the components, the copy you were given, and where each
   icon, vector and sound goes.
3. Search for every icon and vector name and read its description.
4. Build it with tokens and the libraries' own exports.
5. Run `npx @hugocxl/ai check`, fix every error, and look at the result in light and dark at
   phone and desktop widths.

## What `npx @hugocxl/ai check` catches

Errors: icon or vector names that do not exist, sound names that do not exist, imports from
other icon libraries, and agent files that are out of date with the installed libraries.
Warnings: Tailwind's default palette and raw color values in a project that uses the design
system. Run `npx @hugocxl/ai check --help` for options.
