---
version: alpha
name: Design system
description: The personal design system of @hugocxl, the signature shared by every @hugocxl project. Large reading type, vectors and icons from the @hugocxl stack, mono labels and one scarce orange accent.
colors:
  primary: "#171717"
  accent: "#fe9369"
  light:
    canvas: "#f5f5f4"
    ink: "#171717"
    muted: "#6e6e6e"
    faint: "#b3b3b3"
    rule: "#1717171f"
    surface: "#ebebea"
    accent-text: "#ce7755"
    red: "#c43d3d"
    orange: "#bb702f"
    yellow: "#a08005"
    green: "#419445"
    teal: "#378f99"
    sky: "#388cb0"
    blue: "#3f83ce"
    violet: "#633cc7"
    purple: "#993ab8"
    pink: "#c23b62"
    brown: "#8f6d53"
    success: "#419445"
    warning: "#a08005"
    error: "#c43d3d"
    info: "#3f83ce"
    neutral: "#6e6e6e"
  dark:
    canvas: "#111111"
    ink: "#ededed"
    muted: "#7d7d7d"
    faint: "#737373"
    rule: "#ededed24"
    surface: "#1c1c1c"
    accent-text: "#fe9369"
    red: "#c43d3d"
    orange: "#c77b3b"
    yellow: "#ceab3c"
    green: "#4b9d4e"
    teal: "#4da3ad"
    sky: "#4c9fc3"
    blue: "#3f83ce"
    violet: "#7350dc"
    purple: "#9e3fbd"
    pink: "#c23b62"
    brown: "#8f6d53"
    success: "#4b9d4e"
    warning: "#ceab3c"
    error: "#c43d3d"
    info: "#3f83ce"
    neutral: "#7d7d7d"
typography:
  title:
    fontFamily: Geist Sans
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.02em
  reading:
    fontFamily: Geist Sans
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: -0.01em
  heading:
    fontFamily: Geist Sans
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.01em
  small:
    fontFamily: Geist Sans
    fontWeight: 300
    lineHeight: 1.4
  control:
    fontFamily: Geist Sans
    fontSize: 16px
    fontWeight: 400
    letterSpacing: -0.01em
  label:
    fontFamily: Geist Mono
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.08em
  mono:
    fontFamily: Geist Mono
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
  wordmark:
    fontFamily: Geist Sans
    fontSize: 18px
    fontWeight: 600
    letterSpacing: -0.055em
rounded:
  control: 6px
  media: 12px
  pill: 999px
spacing:
  space-1: 4px
  space-2: 8px
  space-3: 12px
  space-4: 16px
  space-5: 20px
  space-6: 32px
  space-7: 40px
  space-8: 56px
  space-9: 80px
  space-10: 128px
  paragraph: 20px
  section: 40px
  figure: 56px
  target: 44px
  measure: 30em
  wide: 80rem
components:
  button:
    backgroundColor: "{colors.light.ink}"
    textColor: "{colors.light.canvas}"
    typography: "{typography.control}"
    rounded: "{rounded.control}"
    height: "{spacing.target}"
    padding: "{spacing.space-5}"
  button-dark:
    backgroundColor: "{colors.dark.ink}"
    textColor: "{colors.dark.canvas}"
    typography: "{typography.control}"
    rounded: "{rounded.control}"
  media:
    backgroundColor: "{colors.light.surface}"
    rounded: "{rounded.media}"
  media-dark:
    backgroundColor: "{colors.dark.surface}"
    rounded: "{rounded.media}"
  code:
    backgroundColor: "{colors.light.surface}"
    textColor: "{colors.light.ink}"
    typography: "{typography.mono}"
    rounded: "{rounded.control}"
  label:
    textColor: "{colors.light.muted}"
    typography: "{typography.label}"
  label-dark:
    textColor: "{colors.dark.muted}"
    typography: "{typography.label}"
  status-dot:
    backgroundColor: "{colors.accent}"
    rounded: "{rounded.pill}"
  status-dot-success:
    backgroundColor: "{colors.light.success}"
    rounded: "{rounded.pill}"
  status-dot-warning:
    backgroundColor: "{colors.light.warning}"
    rounded: "{rounded.pill}"
  status-dot-error:
    backgroundColor: "{colors.light.error}"
    rounded: "{rounded.pill}"
  status-dot-info:
    backgroundColor: "{colors.light.info}"
    rounded: "{rounded.pill}"
  statement-accent:
    textColor: "{colors.light.accent-text}"
    typography: "{typography.title}"
  statement-accent-dark:
    textColor: "{colors.dark.accent-text}"
    typography: "{typography.title}"
  hairline:
    backgroundColor: "{colors.light.rule}"
  hairline-dark:
    backgroundColor: "{colors.dark.rule}"
  placeholder:
    textColor: "{colors.light.faint}"
    typography: "{typography.reading}"
  placeholder-dark:
    textColor: "{colors.dark.faint}"
    typography: "{typography.reading}"
---
## Overview

This is the personal design system of @hugocxl: the signature shared by every @hugocxl project, so each one reads as part of the same body of work. Large reading type leads every page. Line vectors from `@hugocxl/vectors`, icons from `@hugocxl/icons` and monospaced labels make it feel engineered, and a single orange accent appears at most twice per page. The visual reference is Superlogical: its paper and orange, its 21 px reading size, its centered or left-aligned column with a textured field, and its mono footer.

This file and [index.html](index.html) define the system completely. Anything not described here is not part of the system. When you build a page:

1. Pick a recipe from [Page recipes](#page-recipes). The recipe sets the layout and the order of components.
2. For each block, copy the component markup from [Components](#components) exactly. Change only text, links, vector and icon names and IDs.
3. Check the result against [Do's and Don'ts](#dos-and-donts).

Files: `system/ds.css` (all styles), `system/theme.js` (theme, loaded in the head), `system/ds.js` (copy buttons, loaded as a module), `system/fonts/`, `system/images/gray-folds.png` (field texture) and `system/plan.schema.json` (page plan schema). They ship together in the npm package `@hugocxl/design-system`. The package also ships the tokens alone for other stacks, generated from `system/ds.css`: `@hugocxl/design-system/tailwind` (Tailwind v4), `/tailwind-preset` (Tailwind v3), `/tokens.css` and `/fonts.css` (plain CSS), `pkg:@hugocxl/design-system/scss` (Sass) and `/tokens` or `/tokens.json` (JavaScript). In Tailwind, use the token utilities (`bg-canvas`, `text-ink`, `text-reading`, `p-space-5`, `rounded-media`, `max-w-measure`) and never Tailwind's default palette, sizes or radii. Figures come from [`@hugocxl/vectors`](#vectors) and icons from [`@hugocxl/icons`](#icons); no other artwork is part of the system.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Page title</title>
  <link rel="stylesheet" href="system/ds.css">
  <script src="system/theme.js"></script>
  <script type="module" src="system/ds.js"></script>
</head>
<body class="ds" data-layout="plain">
  <!-- masthead -->
  <main>
    <article class="ds-column ds-opening">
      <!-- title, meta, sections, figures, form … in recipe order -->
    </article>
  </main>
  <!-- footer -->
</body>
</html>
```

## Colors

The paper and orange come from Superlogical, and the greys are neutral. Use colors only through these roles. The CSS custom property is `--ds-<role>`, and each one switches with `data-theme` on `<html>`.

| Role | Light | Dark | Use |
| --- | --- | --- | --- |
| `canvas` | `#f5f5f4` | `#111111` | Page background |
| `ink` | `#171717` | `#ededed` | Text and the filled button |
| `muted` | `#6e6e6e` | `#7d7d7d` | Byline, section headings, labels, supporting sentences |
| `faint` | `#b3b3b3` | `#737373` | Placeholder text only |
| `rule` | `#1717171f` | `#ededed24` | Hairlines and borders |
| `surface` | `#ebebea` | `#1c1c1c` | Figure media and code backgrounds |
| `accent` | `#fe9369` | `#fe9369` | The status dot (`.ds-dot`) |
| `accent-text` | `#ce7755` | `#fe9369` | One phrase at title size (`.ds-accent`) |

The system keeps Superlogical's warm paper and orange but uses neutral greys instead of its green-tinted ink and muted tones. Superlogical's muted grey `#b3b3b3` fails WCAG AA for text, so it survives only as the light `faint` for placeholders, and `muted` is set to reach 4.5:1. The orange reaches 3:1 on paper only at title size, which is why `accent-text` exists and is used only there.

**Accent budget:** at most two accent elements per page. That is one `.ds-accent` phrase of two or three words at the end of the `statement`, and one `.ds-dot` before a status label in `meta`. The accent never colors body text, links, buttons, backgrounds, rules or figures.

### Hues

Eleven hues color marks: [colored icons](#colored-icons) and status dots. They take after the [diffs.com icon palette](https://diffs.com/icons). The dark values are the reference's own, with violet and purple lifted to reach contrast. The light values are deepened along the same hue. Every hue reaches 3:1, the WCAG minimum for non-text marks, on both `canvas` and `surface` in its theme. The CSS custom property is `--ds-<hue>`.

| Hue | Light | Dark | For example |
| --- | --- | --- | --- |
| `red` | `#c43d3d` | `#c43d3d` | npm, Ruby, YAML, errors |
| `orange` | `#bb702f` | `#c77b3b` | HTML, Rust, Swift, RSS |
| `yellow` | `#a08005` | `#ceab3c` | JavaScript, folders, archives, warnings |
| `green` | `#419445` | `#4b9d4e` | Shell, tables, Vue, success |
| `teal` | `#378f99` | `#4da3ad` | Prettier, formatters |
| `sky` | `#388cb0` | `#4c9fc3` | Go, React, servers, layers |
| `blue` | `#3f83ce` | `#3f83ce` | TypeScript, C, Docker, code, information |
| `violet` | `#633cc7` | `#7350dc` | CSS, ESLint, Bootstrap, WebAssembly |
| `purple` | `#993ab8` | `#9e3fbd` | Vite, Astro, fonts, MCP |
| `pink` | `#c23b62` | `#c23b62` | GraphQL, Sass, images |
| `brown` | `#8f6d53` | `#8f6d53` | Bun |

Grey is not a hue: an uncolored icon takes the text color, and `neutral` covers the grey status.

- Hues color marks only: an icon (`.ds-icon`) or a dot (`.ds-dot`). Never text, links, buttons, backgrounds, rules, figures or vectors.
- A hue names a kind of thing, the same one everywhere: a language, a tool, a file type or a brand. Never pick a hue for decoration or variety.
- The hues are not the accent. `orange` is a file-type color, and it never replaces `accent`. Hues do not count toward the accent budget.

### Status

Five roles give a hue a meaning. Each is an alias, `--ds-<role>`, so it follows the theme.

| Role | Hue | Light | Dark | Means |
| --- | --- | --- | --- | --- |
| `success` | `green` | `#419445` | `#4b9d4e` | Done, live, passing, confirmed |
| `warning` | `yellow` | `#a08005` | `#ceab3c` | Needs attention soon but still works |
| `error` | `red` | `#c43d3d` | `#c43d3d` | Failed, down, invalid, blocked |
| `info` | `blue` | `#3f83ce` | `#3f83ce` | Scheduled, planned, worth knowing |
| `neutral` | `muted` | `#6e6e6e` | `#7d7d7d` | Inactive: draft, paused, archived |

Set `data-status` on a `.ds-dot`, a `.ds-icon` or the form's `.ds-feedback` and it takes the role's color. A `.ds-dot` without `data-status` stays the accent.

| Status label | Role | Mark |
| --- | --- | --- |
| Live, Stable, Operational, Shipped, Paid, Sent | `success` | dot, or `circle-check` |
| Degraded, Deprecated, Expiring, Limited | `warning` | dot, or `triangle-alert` |
| Down, Failed, Removed, Overdue, Invalid | `error` | dot, or `circle-x` |
| Planned, Scheduled, Maintenance, Preview | `info` | dot, or `circle-info` |
| Draft, Paused, Archived, Unlisted | `neutral` | dot |
| Beta, New (the page's own status in `meta`) | accent | `.ds-dot` without `data-status` |

- Color never carries a status alone. The words always name it, and the dot or icon goes before them.
- Status text stays `ink`, or `muted` where the component already uses it. Only the mark takes the color.
- One status per element and one mark per status: a dot or an icon, never both.
- A status mark goes where a status label goes: a `meta` label, an `index` label, a table cell or the form feedback line.

## Typography

Geist Sans for everything people read and Geist Mono for labels, dates and code. Both are bundled as variable WOFF2 files. Use three weights: 300 for reading, 400 for headings and controls, and 500 for the title and `<strong>`. The wordmark alone uses 600.

| Style | Size | Weight | Line height | Tracking | Use |
| --- | --- | --- | --- | --- | --- |
| title | `1.4 × reading` (≈ 29.7px at 1440) | 500 | 1.15 | −0.02em | `title`, `statement`. The largest text on any page. |
| reading | `min(1rem + 0.36vw, 1.54rem)` (≈ 21.2px at 1440) | 300 | 1.3 | −0.01em | Body text |
| heading | reading | 400, muted | 1.3 | −0.01em | Section `h2`, item `h3` (in ink) |
| small | `0.8 × reading` | 300 | 1.4 | −0.01em | Grid item text, table cells |
| label | 13px mono, uppercase | 400 | 1.5 | 0.08em | Dates, versions, figure captions, table headings |
| mono | 15px mono | 400 | 1.4 | 0 | Footer links |
| control | 16px | 400 | 1 | −0.01em | Button text |

Supporting sentences follow the main thought in the same paragraph, wrapped in `<span class="ds-muted">`. Write in sentence case.

## Layout

Set the layout with `data-layout` on `<body class="ds">`. There are two layouts:

- **`plain`** is the default for every page, home included. The column is centered, and wide figures are centered on the column. Nothing sits beside the content.
- **`field`** is an optional signature for a personal home page, such as hugocxl.me, and nowhere else. The column aligns to the left gutter and a fixed textured panel fills the right side at `clamp(30vw, 100vw − 2 × gutter − 47.6rem, 40vw)`, inset 12px with a 12px radius. At 760px and below the field becomes a 12px strip. Never use it on product, library or documentation sites.

The column (`.ds-column`) is 30em of reading type, about 65 characters. `.ds-wide` elements (figures and grids) extend to `min(main width, 80rem)`. The gutter is `clamp(1.25rem, 4.5vw, 4rem)`. The opening padding is `clamp(80px, 8vw, 128px)`.

Use only these ten spacing steps:

| Token | Value | Role |
| --- | --- | --- |
| `space-1` | 4px | — |
| `space-2` | 8px | List items, label gaps, item title to text |
| `space-3` | 12px | Caption offset, table cell padding |
| `space-4` | 16px | Section heading to text |
| `space-5` | 20px | Between paragraphs |
| `space-6` | 32px | Title to meta, masthead top, grid gutter |
| `space-7` | 40px | Between sections, form top |
| `space-8` | 56px | Around wide figures, meta to lead |
| `space-9` | 80px | Above the footer |
| `space-10` | 128px | Largest opening |

### Page recipes

A recipe fixes the layout and the component order. `?` means optional, `+` one or more, `*` zero or more and `|` one of. The first `section` after `title`, `statement` or `meta` has no heading and acts as the lead. Leave out an optional component when the brief has no content for it.

| Recipe | Layout | Sequence |
| --- | --- | --- |
| `home` | plain (field on a personal site) | `masthead statement meta? section (figure-wide \| figure-grid) section* (button \| form)? footer` |
| `article` | plain | `masthead title meta section figure-wide? section+ form? footer` |
| `docs` | plain | `masthead title meta? section (section \| figure-wide)* footer` |
| `changelog` | plain | `masthead title section? index footer` |
| `pricing` | plain | `masthead title section index table? section* button footer` |
| `contact` | plain | `masthead title section form footer` |

`masthead` goes before `<main>` and `footer` after it. All other components go inside `<article class="ds-column ds-opening">`, in order. The example home page in [index.html](index.html#recipes) is the reference output.

## Product interfaces

Pages are read; product interfaces are worked in. A tool such as an editor, a console or an inspector keeps every token, role and rule above and adds what long sessions with a pointer need. The [`@hugocxl/components`](https://hugocxl.github.io/stack/components/) library builds all of it for SwiftUI; set `.dsDensity(.compact)` at the root of a desktop tool.

### Density

Two densities set the same system at two sizes. Never mix them in one window.

| Density | Reading | Small | Label | Title | Control | Target | For |
| --- | --- | --- | --- | --- | --- | --- | --- |
| regular | 17pt (21px web) | 0.8× | 13px mono | 1.4× | 16 | 44 | Pages, documents and touch screens |
| compact | 13pt | 11pt | 10pt mono | 17pt | 13 | 28 | Pointer-driven desktop tools |

**One text size.** Product interfaces set everything at the reading size: body, controls, field values, property labels, help, mono labels and figures. Styles differ by face, weight, case and tone, never by size. Two exceptions, each with a reason: the title, once per screen, and display figures read at a distance on a screen or a readout. A smaller or larger size anywhere else needs the same kind of reason, written down.

**One spacing unit.** A product interface is laid out on one unit: `space-4` (16pt) regular, `space-3` (12pt) compact. Every padding, margin and gap between elements is the unit: a cell's padding, the gap between a label and its control, between controls in a row, between a title and its tools. Rows and sections add nothing between them; they meet on a hairline. Smaller steps live only inside a component, such as the gap between an icon and its words.

**Control height.** Every single-line control is exactly the control height, the target: 44pt regular, 28pt compact. That covers buttons, icon buttons, selects, text and search fields, menu triggers, segmented controls, slider tracks, the rows of switches, checkboxes and radios, a rack's tab and the readout of a transport. Never make a control taller or shorter, so any row of mixed controls lines up. Only content grows: a multiline field, a row with a description, a key that shows a picture.

### Workspace

A product window is one canvas divided into panes, like an instrument panel.

- **Panes** fill the window edge to edge. They have no corners, no fill of their own, no gap and no shadow. One `rule` hairline divides neighbours.
- **Cartesian grid.** Everything inside a pane is split by a grid of bordered cells, like a camera's settings screen. Hairlines run edge to edge between rows and columns and meet the pane's edges. Each cell is padded by the unit and carries its mono label top-left, with its content one unit below. A cell takes the whole row unless it spans fewer columns; the last cell of a row stretches to its end, so every row is whole. No gutters: spacing lives inside cells.
- **Section.** Every group of settings is the same section: a three-column grid whose first row is the header cell (the name in ink, its reset and power tools at the trailing end), then one cell per parameter. Knobs take one column each, three to a row; selects, fields, key grids, switches and notes take the row. A sub-group is a label cell across the row. Sections follow one another with no space between them. The same section serves inspectors, settings and dialogs: never invent a different one.
- **Pane header**: an optional muted icon, the pane's name as a mono `label`, and its tools at the trailing end, over a hairline. A pane's name is never a title.
- **Toolbar**: one row above the workspace with leading, centered and trailing groups of ghost icon buttons, divided by short hairlines, over a hairline. The window's one filled button lives here or in a dialog.
- **Inspector**: a stack of sections. A property row in a grid becomes a cell, its label top-left and its control below. Controls hide their own label; the cell names them.
- **Empty pane**: a vector from `@hugocxl/vectors`, a heading, one muted sentence and the action that fills it, left aligned.
- **Media viewers** that people judge color in keep a fixed dark neutral surround in both themes instead of `surface`. Words and marks drawn over that surround use the dark theme's tokens.

### States

| State | Mark |
| --- | --- |
| Hover | `surface` behind the control or row |
| Selected row | `surface` behind, words and icon in `ink` |
| Open pane, toggle on | The cap stays pressed into its well, words and icon in `ink` |
| Pressed | The cap sinks: no rest shadow, the inner shadow |
| Focus | 2px `ink` outline with a 3px offset |
| Disabled | 40% opacity |
| Destructive action | words in `error` on a hairline button; never the filled button |

Selection and on states never use the accent.

### Instruments

The accent marks the live position of an instrument, one mark per instrument: the slider's pointer, the knob's dot, a timeline's playhead, a recording light. It does not count toward the page's accent budget, and it never fills, labels or selects anything.

Sliders that change a document group a whole gesture (drag, reset or typed value) into one undo step. Double-clicking the track resets to the default; double-clicking the reading types an exact value.

**Knobs first.** Every continuous numeric parameter is a knob: amounts, levels, times, ratios, frequencies. A knob in a grid cell shows its name top-left, the dial centred below and its reading under the dial. Sliders stay for scrubbing time or position along a line; faders only where a level is ridden live.

Instruments come from hardware and audio plugins:

- **Knob**: a disc in a ring of ticks, or in a hairline arc drawn over in ink up to the value. Centered knobs grow both ways from twelve o'clock for values around zero. Drag up or right to turn, double-click to reset, double-click the reading to type.
- **Fader**: upright, as on a console, for levels people ride: a well that fills with ink from the bottom. A vertical LED meter may stand beside it to show a live level.
- **Slider**: a hairline track drawn over in ink up to a small round thumb, for a value inside a property row.
- **Meter**: LED segments in an inset strip, horizontal or upright, lit in the accent or a status tone.
- **Rack**: a hairline frame that holds the instruments of one processor, named in a notch cut into its top edge. With pages, the tab steps through them and dots show where you are. Racks hold instruments only and never nest.

### Displays

What an instrument shows is drawn apart from what you touch.

- **Screen**: an LCD. Dark glass in a well, in both themes, with its type and marks lit in the accent. Labels are dim, values lit. Mode tabs run along its top, the picked one lit. Levels over time are columns of LED segments. Screens show live readouts, levels and status, never forms.
- **Data table**: a light well of mono rows under a mono header and a dashed rule. The row the instrument is on (playing, rendering, focused) is lit in the accent between two dashes, like a cursor.
- **Drum**: a select for an ordered list, like a hardware roller. A short column of options fades away from the picked one, which is lit between two accent marks. Drag, scroll or click a neighbour to turn it.
- **LEDs**: a hardware selector may show a dot under each position, lit under the picked one.

On a screen, in a data table and on a drum, the accent is the light of the display, the same way it is the live mark of an instrument.

### Editorial

Product sheets and the quieter parts of an app take after a printed product catalogue:

- **Space first.** Let a section breathe: `space-8` between sections, one idea each, the figure or product on `surface` with nothing else around it.
- **Eyebrows.** A section may open with a mono uppercase label, an icon before it, spaced at 0.1em, above a one-line title.
- **Specifications.** Facts people check are a spec list: a mono uppercase label in `muted` beside its value, one fact per row, between hairlines. Never a paragraph of figures.
- **Features.** Two to four features read across in a row: an icon, a mono uppercase name, one muted sentence.

### Data marks

Items people read by kind at a glance, such as clips in a timeline, tracks or chart series, are data marks: `surface` with the kind's hue at 16% over it and a 1px edge of the hue. This is the only place a hue tints a fill. The words on a mark stay `ink` and say what it is; selection is a 2px `ink` edge. The same kind keeps the same hue everywhere.

### Sound

Product interfaces may confirm direct actions with [`@hugocxl/sounds`](https://hugocxl.github.io/stack/sounds/): `down` and `up` for a press, `latch-down` and `latch-up` for a toggle, `tick` for a detent, segment or disclosure, `open` for a dialog, and `success`, `warning` or `error` for the result of an action. Sound never carries information alone, never plays for hover or anything people did not do, and people can always turn it off.

## Elevation & Depth

Layout is flat: group content with space and `rule` hairlines, never with cards. Controls are quietly physical, after minimal audio plugins: a pale chassis, controls drawn in hairlines and ink that sit a hair above it, and almost no colour.

### Material

| Part | What it is | How it is drawn |
| --- | --- | --- |
| Chassis | `canvas`, the body everything is built on | Flat. Panes, sections and text sit on it. |
| Cap | Something you touch: a button, an icon button, a knob, a slider thumb, a switch knob, the picked segment, a select | A hair above: `plate` fill, a hairline and one soft shadow |
| Well | Something that holds a value: a text field, a fader, a switch or segmented track, a meter, a checkbox | A shade below: `well` fill and a hairline, no shadow |
| Screen | Media and data people look into: a viewer, a timeline, a graph | Flat, edge to edge, no padding or radius in a product interface |

| Token | Light | Dark |
| --- | --- | --- |
| `plate` | `#fcfcfb` | `#1f1f1f` |
| `well` | `#efefee` | `#171717` |
| Rest shadow (under a cap) | black at 6%, 3px blur, 1px down | black at 35%, 3px blur, 1px down |
| Lift (dialogs and menus) | black at 10%, 24px blur, 12px down | black at 45%, 24px blur, 12px down |

- **Restraint.** One soft shadow under a cap, a hairline around everything. No sheen, no highlights, no inner shadows, no gradients, no glow.
- **Pressing sinks.** A pressed cap loses its shadow and takes the well's shade. A toggle that is on, and a toolbar button whose pane is open, stay pressed in.
- **Caps are small.** Only controls sit up. Never raise a pane, a section, text or a figure.
- **Instruments are drawn in ink**: a knob's arc and pointer, a slider's track, a fader's bar. The accent lights only what is live: the playhead, recording, a lit screen, an LED.

## Shapes

Radii: 6px for the button, code blocks and table edges, 12px for media and the field, and a pill for the pager. Hairlines are 1px `rule`. Interactive targets are at least 44 × 44px. Focus is a 2px `ink` outline with a 3px offset.

## Components

These thirteen components make up the whole vocabulary. Each markup block below is copied from the live specimen in `index.html` by `pnpm run sync`, so it is exactly what the reference renders. Keep every class and attribute.

### `masthead`

Wordmark, up to three text links, and the theme button with the `contrast` icon. It is the first element in the body.

<!-- specimen:masthead -->
```html
<header class="ds-masthead">
  <a class="ds-wordmark" href="/">Fieldwork</a>
  <a href="/changelog">Changelog</a>
  <a href="/docs">Docs</a>
  <button class="ds-theme" type="button" data-ds-theme aria-label="Switch theme"><svg class="ds-icon" data-icon="contrast" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg></button>
</header>
```
<!-- /specimen -->

### `title`

The page name in ink with a muted byline. Use it on every recipe except home. The heading fits on one line.

<!-- specimen:title -->
```html
<hgroup class="ds-title">
  <h1>Public testing is beginning</h1>
  <p>Fieldwork team</p>
</hgroup>
```
<!-- /specimen -->

### `statement`

Home only: one sentence at title size, ending with an optional accent phrase of two or three words.

<!-- specimen:statement -->
```html
<h1 class="ds-statement">Field notes for teams that ship <span class="ds-accent">every day.</span></h1>
```
<!-- /specimen -->

### `meta`

One to three mono labels: status, version, date. Only a status label takes `.ds-dot`, and it comes first. The page's own status (Beta, New) uses the accent dot. A state from [Status](#status) sets `data-status` on the dot, as in `<span class="ds-dot" data-status="success" aria-hidden="true"></span>Operational`. Dates use `<time datetime>`.

<!-- specimen:meta -->
```html
<ul class="ds-meta">
  <li class="ds-label"><span class="ds-dot" aria-hidden="true"></span>Beta</li>
  <li class="ds-label"><time datetime="2026-10-05">5 October 2026</time></li>
</ul>
```
<!-- /specimen -->

### `section`

A muted `h2` followed by paragraphs, lists, `code` or `table`. The lead section has no `h2`. Give a section an `id` when the page links to it.

<!-- specimen:section -->
```html
<section class="ds-section" id="what-is-available">
  <h2>What is available</h2>
  <p>Initially, testing is limited to the macOS application. <span class="ds-muted">Linux and Windows follow once the first wave is stable.</span></p>
  <p>Read the <a href="/docs">documentation</a> for setup.</p>
</section>
```
<!-- /specimen -->

### `figure-wide`

One [vector](#vectors) or, for a product screenshot, an `<img>` on the surface at 3:2, with a caption that reads `Fig. NN / Name`. A vector keeps its `title`; an image needs `alt`. Add the pager, with `arrow-left` and `arrow-right` icons, only when the figure cycles.

<!-- specimen:figure-wide -->
```html
<figure class="ds-wide">
  <div class="ds-media"><svg class="ds-vector" data-vector="how-it-works" viewBox="0 0 480 360" role="img" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"><title>How it works</title><!-- paths from @hugocxl/vectors --></svg></div>
  <figcaption class="ds-caption"><span class="ds-label">Fig. 01 / How it works</span></figcaption>
</figure>
```
<!-- /specimen -->

### `figure-grid`

Two to four [vectors](#vectors) separated by hairlines. Each has a `Fig 0.N` label, a title of up to four words and one sentence. Set `data-columns` to the item count. The grid stacks when its container is narrower than 34rem.

<!-- specimen:figure-grid -->
```html
<ul class="ds-grid ds-wide" data-columns="3">
  <li>
    <span class="ds-label">Fig 0.1</span>
    <svg class="ds-vector" data-vector="modular-design" viewBox="0 0 480 360" role="img" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"><title>Modular design</title><!-- paths from @hugocxl/vectors --></svg>
    <h3>Purpose-built</h3>
    <p>Shaped by the practices of teams who ship daily.</p>
  </li>
  <li>
    <span class="ds-label">Fig 0.2</span>
    <svg class="ds-vector" data-vector="handoff" viewBox="0 0 480 360" role="img" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"><title>Handoff</title><!-- paths from @hugocxl/vectors --></svg>
    <h3>Shared by people and agents</h3>
    <p>From the first draft to the merged change.</p>
  </li>
  <li>
    <span class="ds-label">Fig 0.3</span>
    <svg class="ds-vector" data-vector="fast-performance" viewBox="0 0 480 360" role="img" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"><title>Fast performance</title><!-- paths from @hugocxl/vectors --></svg>
    <h3>Designed for speed</h3>
    <p>Less noise, more momentum, every release.</p>
  </li>
</ul>
```
<!-- /specimen -->


### `index`

Rows divided by hairlines for changelogs, steps, plans and principles. The label is a number (`01`), a date or a price.

<!-- specimen:index -->
```html
<ol class="ds-index">
  <li><span class="ds-label"><time datetime="2026-11-12">12 Nov 2026</time></span><div><h3>Persistent sessions</h3><p>Sessions survive restarts and reconnect where you left them.</p></div></li>
  <li><span class="ds-label"><time datetime="2026-10-28">28 Oct 2026</time></span><div><h3>Remote hosts</h3><p>Connect to any machine running the server.</p></div></li>
</ol>
```
<!-- /specimen -->

### `table`

Comparisons and specifications. Column headings use `scope="col"` and row headings use `scope="row"`. Always wrap the table in `.ds-table-scroll` with `tabindex="0"` so it can be scrolled by keyboard.

<!-- specimen:table -->
```html
<div class="ds-table-scroll" tabindex="0">
  <table class="ds-table">
    <thead><tr><th scope="col">Plan</th><th scope="col">Price</th><th scope="col">Hosts</th></tr></thead>
    <tbody>
      <tr><th scope="row">Personal</th><td>Free</td><td>3</td></tr>
      <tr><th scope="row">Team</th><td>€12 per seat / month</td><td>Unlimited</td></tr>
    </tbody>
  </table>
</div>
```
<!-- /specimen -->

### `button`

The single filled action on a page. Use `<a>` for navigation and `<button type="button">` for an in-place action. Every other action is an underlined text link.

<!-- specimen:button -->
```html
<a class="ds-button" href="/download">Download for macOS</a>
```
<!-- /specimen -->

### `form`

A visible label, an underlined input with an icon submit button (`corner-down-left` to send or `arrow-right` to go, with an `aria-label`), optional help text and a live feedback line.

| State | Result |
| --- | --- |
| Idle | Placeholder in `faint`, feedback empty |
| Invalid submit | Value kept, `aria-invalid="true"` on the input (a wavy `error` underline), `data-status="error"` on the feedback, the fix written in the feedback line |
| Editing after an error | `aria-invalid` and `data-status` removed, feedback cleared |
| Pending | Submit disabled, no `data-status`, feedback reads “Sending…” |
| Success | `data-status="success"` on the feedback, which confirms in one sentence. Focus stays on the input. |
| Failure | Value kept, `data-status="error"` on the feedback, which explains the failure and how to retry |

With `data-status`, the feedback line starts with a dot in the status color. Its text stays `ink`.

<!-- specimen:form -->
```html
<form class="ds-form" action="/waitlist" method="post">
  <label for="waitlist-email">Sign up to secure your place in the waitlist</label>
  <div class="ds-input">
    <input type="email" id="waitlist-email" name="email" placeholder="you@example.com" required autocomplete="email" aria-describedby="waitlist-help waitlist-feedback">
    <button type="submit" aria-label="Join the waitlist"><svg class="ds-icon" data-icon="corner-down-left" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg></button>
  </div>
  <p class="ds-help" id="waitlist-help">We’ll let you know when the beta is available.</p>
  <output class="ds-feedback" id="waitlist-feedback" aria-live="polite"></output>
</form>
```
<!-- /specimen -->

### `code`

A command or snippet on the surface with a Copy button. `system/ds.js` handles the copy. `tabindex="0"` on `pre` keeps long lines scrollable by keyboard.

<!-- specimen:code -->
```html
<div class="ds-code"><pre tabindex="0"><code>brew install fieldwork</code></pre><button type="button">Copy</button></div>
```
<!-- /specimen -->

### `footer`

Mono links at both ends with a hairline between them. It is the last element in the body, after `</main>`.

<!-- specimen:footer -->
```html
<footer class="ds-footer">
  <ul><li><a href="/press">Press kit</a></li></ul>
  <ul><li><a href="/privacy">Privacy</a></li><li><a href="https://x.com/fieldwork">@fieldwork</a></li></ul>
</footer>
```
<!-- /specimen -->

## Icons and vectors

Pages draw with two companion libraries and nothing else. [`@hugocxl/icons`](https://hugocxl.github.io/stack/icons/) label actions and [`@hugocxl/vectors`](https://hugocxl.github.io/stack/vectors/) illustrate ideas. Both draw in `currentColor`, so they follow the theme and never touch the accent. Only an icon may take a color, from the [hues](#hues) or the [status roles](#status). No other icon set, illustration, emoji or symbol character may stand in for them.

```sh
npm install @hugocxl/design-system @hugocxl/icons @hugocxl/vectors
```

In the markup above, `<!-- paths from @hugocxl/icons -->` and `<!-- paths from @hugocxl/vectors -->` mark where the SVG's own content goes. Copy it from the package: the JavaScript export of each name is the SVG as a string, and the React components render it directly.

### Icons

Use the **Stroke** style. An icon either goes before the words of a link, the `button` or a `meta` label, or it is the whole content of an icon button that has an `aria-label`. Give the SVG `class="ds-icon"` and `data-icon` with its name: it sizes to `1em`, takes the text color and keeps `space-2` before the words. Inside an icon button the gap is removed.

```html
<!-- Before words -->
<a href="/docs"><svg class="ds-icon" data-icon="book-open" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg>Read the guide</a>
<a class="ds-button" href="/browse"><svg class="ds-icon" data-icon="search" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg>Browse icons</a>
<li class="ds-label"><svg class="ds-icon" data-icon="calendar" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg><time datetime="2026-11-18">18 November 2026</time></li>

<!-- Alone, in an icon button -->
<button class="ds-theme" type="button" data-ds-theme aria-label="Switch theme"><svg class="ds-icon" data-icon="contrast" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg></button>
```

```jsx
import { BookOpenIcon } from '@hugocxl/icons/react/stroke';

<a href="/docs"><BookOpenIcon className="ds-icon" />Read the guide</a>
```

| Place | Icon |
| --- | --- |
| Theme button | `contrast` |
| Pager | `arrow-left`, `arrow-right` |
| Form submit | `corner-down-left` to send, `arrow-right` to go |
| Search | `search` |
| External link | `arrow-up-right` |

- One icon per element. Before words it never replaces a word; alone it needs an `aria-label`.
- Only in links, the button, meta labels and icon buttons, plus [colored icons](#colored-icons) in index labels and table cells. Never in headings, the statement, body sentences or the footer.
- Icons carry `aria-hidden="true"`. The React components add it unless they receive an `aria-label`.
- Never in the accent color, and never draw arrows, ◐ or other symbols as text instead.

### Colored icons

An icon takes a color only when the color carries meaning, in one of two ways:

- **Kind.** `data-color="<hue>"` marks what a thing is: a language, a tool, a file type or a brand, such as `folder` in `yellow` or `terminal` in `green`. Use the hue the icon library assigns to the icon, so the same thing has the same color everywhere. These icons label items in a list, an `index` label or a table cell.
- **Status.** `data-status="<role>"` marks a state, before the words that name it: `circle-check` for `success`, `triangle-alert` for `warning`, `circle-x` for `error`, `circle-info` for `info`.

```html
<!-- Kind: what the item is -->
<td><svg class="ds-icon" data-icon="folder" data-color="yellow" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg>components</td>

<!-- Status: the state, named by the words after it -->
<li class="ds-label"><svg class="ds-icon" data-icon="circle-check" data-status="success" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg>Operational</li>
```

Colored icons can use the Duotone style, whose second layer is the same color at lower opacity, as well as Stroke. Everything else follows the icon rules above.

- Action icons, such as those in links, the button and icon buttons, are never colored. They take the text color.
- One color per icon, from the tokens. Never a hex value, a gradient or the accent.
- The words beside a colored icon always say what it means. Color alone never does.

### Vectors

Every figure is a vector from `@hugocxl/vectors`. It fills `figure-wide` and each `figure-grid` item, drawn in ink on the surface at its own 4:3 proportions. Inline the SVG, replace its root `xmlns` attribute with `class="ds-vector"` and `data-vector` with its name, and remove its `color` attribute.

```html
<figure class="ds-wide">
  <div class="ds-media"><svg class="ds-vector" data-vector="modular-design" viewBox="0 0 480 360" role="img" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"><title>Modular design</title><!-- paths from @hugocxl/vectors --></svg></div>
  <figcaption class="ds-caption"><span class="ds-label">Fig. 02 / Modular design</span></figcaption>
</figure>
```

```jsx
import { ModularDesignVector } from '@hugocxl/vectors/react/modular-design';

<div className="ds-media"><ModularDesignVector className="ds-vector" /></div>
```

- Choose a vector for what it means. The [vectors browser](https://hugocxl.github.io/stack/vectors/browse.html) lists all 2,000 by use case. Name it in the caption.
- Keep the SVG's `title` and `desc`: they are its accessible name.
- Use an `<img>` only for a screenshot of the product itself.
- Never crop a vector, color it with the accent or place it on the field.
- Use the `field` layout only on a personal home page.

## Do's and Don'ts

### Always

- Load `system/ds.css` and `system/theme.js` in the head and `system/ds.js` as a module.
- Set `class="ds"` and the recipe's `data-layout` on the body.
- Follow the recipe's component order. Copy component markup exactly and change only text, links, vector and icon names and IDs.
- Write in sentence case. Keep the title to one line and the statement to one sentence.
- Put supporting sentences in `.ds-muted`, inline after the main thought. Text on `surface` is always `ink`, because muted falls below 4.5:1 there.
- Keep every vector's `title`, give every icon button an `aria-label`, every image `alt` text and every field a visible label.
- Check the page at 320, 760, 761 and 1440px wide in both themes.

### Never

- Never add a class, color, font, size, weight, radius or spacing value that is not a token.
- Never use the accent more than twice, or on body text, links, buttons, backgrounds, rules or figures. In a product interface, the live mark of an instrument is the one addition.
- Never use a hue or status color on anything but an icon, a dot or a data mark, or let color alone say what something is or what state it is in.
- Never set text larger than the title or bolder than 500 (the wordmark is the exception).
- Never use shadows or gradients outside the material: a cap's rest shadow and highlight, a well's inner shadow, or the lift under dialogs and menus. Never use emoji, stock photography, symbol characters as icons, or icons and illustrations from outside `@hugocxl/icons` and `@hugocxl/vectors`. Icons use the Stroke style.
- Never place two filled buttons on one page.
- Never center or justify text. Only the column itself is centered.
- Never invent copy, links, numbers, quotes or logos the brief does not supply. If a required input is missing, ask for it.

### Brief an agent

Give the agent this file at a pinned commit and a page plan. A page plan is JSON that validates against `system/plan.schema.json`. It names the recipe and layout and lists the blocks in order, with every slot filled. Validate the plan, check its sequence against the recipe, and then render each block from its component markup. The model's freedom stays in the plan, so the same plan and revision always produce the same page.

```json
{
  "designRevision": "<design-system commit SHA>",
  "recipe": "changelog",
  "layout": "plain",
  "blocks": [
    { "component": "masthead", "wordmark": "Fieldwork", "links": [{ "label": "Docs", "href": "/docs" }] },
    { "component": "title", "heading": "Changelog", "byline": "What shipped, newest first" },
    { "component": "index", "items": [
      { "label": "12 Nov 2026", "datetime": "2026-11-12", "title": "Persistent sessions", "text": "Sessions survive restarts." }
    ] },
    { "component": "footer", "start": [{ "label": "Press kit", "href": "/press" }], "end": [] }
  ]
}
```

### Verify

`pnpm test` lints this file, checks that its markup matches the specimens, and runs browser tests on the reference: computed tokens in both themes, column and figure geometry at 320, 760, 761 and 1440px, the accent budget, keyboard behavior and an axe WCAG 2.2 AA scan. For a generated page, check the same things plus the recipe order. To compare screenshots, fix the browser, viewport, scale, theme, locale and motion settings, and wait for fonts and figures to load.
