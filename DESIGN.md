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
  dark:
    canvas: "#111111"
    ink: "#ededed"
    muted: "#7d7d7d"
    faint: "#737373"
    rule: "#ededed24"
    surface: "#1c1c1c"
    accent-text: "#fe9369"
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

Files: `system/p9.css` (all styles), `system/theme.js` (theme, loaded in the head), `system/p9.js` (copy buttons, loaded as a module), `system/fonts/`, `system/images/gray-folds.png` (field texture) and `system/plan.schema.json` (page plan schema). They ship together in the npm package `@hugocxl/design-system`. Figures come from [`@hugocxl/vectors`](#vectors) and icons from [`@hugocxl/icons`](#icons); no other artwork is part of the system.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Page title</title>
  <link rel="stylesheet" href="system/p9.css">
  <script src="system/theme.js"></script>
  <script type="module" src="system/p9.js"></script>
</head>
<body class="p9" data-layout="plain">
  <!-- masthead -->
  <main>
    <article class="p9-column p9-opening">
      <!-- title, meta, sections, figures, form … in recipe order -->
    </article>
  </main>
  <!-- footer -->
</body>
</html>
```

## Colors

The paper and orange come from Superlogical, and the greys are neutral. Use colors only through these roles. The CSS custom property is `--p9-<role>`, and each one switches with `data-theme` on `<html>`.

| Role | Light | Dark | Use |
| --- | --- | --- | --- |
| `canvas` | `#f5f5f4` | `#111111` | Page background |
| `ink` | `#171717` | `#ededed` | Text and the filled button |
| `muted` | `#6e6e6e` | `#7d7d7d` | Byline, section headings, labels, supporting sentences |
| `faint` | `#b3b3b3` | `#737373` | Placeholder text only |
| `rule` | `#1717171f` | `#ededed24` | Hairlines and borders |
| `surface` | `#ebebea` | `#1c1c1c` | Figure media and code backgrounds |
| `accent` | `#fe9369` | `#fe9369` | The status dot (`.p9-dot`) |
| `accent-text` | `#ce7755` | `#fe9369` | One phrase at title size (`.p9-accent`) |

The system keeps Superlogical's warm paper and orange but uses neutral greys instead of its green-tinted ink and muted tones. Superlogical's muted grey `#b3b3b3` fails WCAG AA for text, so it survives only as the light `faint` for placeholders, and `muted` is set to reach 4.5:1. The orange reaches 3:1 on paper only at title size, which is why `accent-text` exists and is used only there.

**Accent budget:** at most two accent elements per page. That is one `.p9-accent` phrase of two or three words at the end of the `statement`, and one `.p9-dot` before a status label in `meta`. The accent never colors body text, links, buttons, backgrounds, rules or figures.

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

Supporting sentences follow the main thought in the same paragraph, wrapped in `<span class="p9-muted">`. Write in sentence case.

## Layout

Set the layout with `data-layout` on `<body class="p9">`. There are two layouts:

- **`field`** is for home only. The column aligns to the left gutter. A fixed textured panel fills the right side at `clamp(30vw, 100vw − 2 × gutter − 47.6rem, 40vw)`, inset 12px with a 12px radius. At 760px and below the field becomes a 12px strip.
- **`plain`** is for every other recipe. The column is centered, and wide figures are centered on the column.

The column (`.p9-column`) is 30em of reading type, about 65 characters. `.p9-wide` elements (figures and grids) extend to `min(main width, 80rem)`. The gutter is `clamp(1.25rem, 4.5vw, 4rem)`. The opening padding is `clamp(80px, 8vw, 128px)`.

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
| `home` | field | `masthead statement meta? section (figure-wide \| figure-grid) section* (button \| form)? footer` |
| `article` | plain | `masthead title meta section figure-wide? section+ form? footer` |
| `docs` | plain | `masthead title meta? section (section \| figure-wide)* footer` |
| `changelog` | plain | `masthead title section? index footer` |
| `pricing` | plain | `masthead title section index table? section* button footer` |
| `contact` | plain | `masthead title section form footer` |

`masthead` goes before `<main>` and `footer` after it. All other components go inside `<article class="p9-column p9-opening">`, in order. The example home page in [index.html](index.html#recipes) is the reference output.

## Elevation & Depth

The system is flat. Group content with space and `rule` hairlines. The only fills are `surface` behind media and code, and `ink` behind the one button. Use no shadows, gradients or blur.

## Shapes

Radii: 6px for the button, code blocks and table edges, 12px for media and the field, and a pill for the pager. Hairlines are 1px `rule`. Interactive targets are at least 44 × 44px. Focus is a 2px `ink` outline with a 3px offset.

## Components

These thirteen components make up the whole vocabulary. Each markup block below is copied from the live specimen in `index.html` by `npm run sync`, so it is exactly what the reference renders. Keep every class and attribute.

### `masthead`

Wordmark, up to three text links, and the theme button with the `contrast` icon. It is the first element in the body.

<!-- specimen:masthead -->
```html
<header class="p9-masthead">
  <a class="p9-wordmark" href="/">Fieldwork</a>
  <a href="/changelog">Changelog</a>
  <a href="/docs">Docs</a>
  <button class="p9-theme" type="button" data-p9-theme aria-label="Switch theme"><svg class="p9-icon" data-icon="contrast" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg></button>
</header>
```
<!-- /specimen -->

### `title`

The page name in ink with a muted byline. Use it on every recipe except home. The heading fits on one line.

<!-- specimen:title -->
```html
<hgroup class="p9-title">
  <h1>Public testing is beginning</h1>
  <p>Fieldwork team</p>
</hgroup>
```
<!-- /specimen -->

### `statement`

Home only: one sentence at title size, ending with an optional accent phrase of two or three words.

<!-- specimen:statement -->
```html
<h1 class="p9-statement">Field notes for teams that ship <span class="p9-accent">every day.</span></h1>
```
<!-- /specimen -->

### `meta`

One to three mono labels: status, version, date. Only a status label takes `.p9-dot`, and it comes first. Dates use `<time datetime>`.

<!-- specimen:meta -->
```html
<ul class="p9-meta">
  <li class="p9-label"><span class="p9-dot" aria-hidden="true"></span>Beta</li>
  <li class="p9-label"><time datetime="2026-10-05">5 October 2026</time></li>
</ul>
```
<!-- /specimen -->

### `section`

A muted `h2` followed by paragraphs, lists, `code` or `table`. The lead section has no `h2`. Give a section an `id` when the page links to it.

<!-- specimen:section -->
```html
<section class="p9-section" id="what-is-available">
  <h2>What is available</h2>
  <p>Initially, testing is limited to the macOS application. <span class="p9-muted">Linux and Windows follow once the first wave is stable.</span></p>
  <p>Read the <a href="/docs">documentation</a> for setup.</p>
</section>
```
<!-- /specimen -->

### `figure-wide`

One [vector](#vectors) or, for a product screenshot, an `<img>` on the surface at 3:2, with a caption that reads `Fig. NN / Name`. A vector keeps its `title`; an image needs `alt`. Add the pager, with `arrow-left` and `arrow-right` icons, only when the figure cycles.

<!-- specimen:figure-wide -->
```html
<figure class="p9-wide">
  <div class="p9-media"><svg class="p9-vector" data-vector="how-it-works" viewBox="0 0 480 360" role="img" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"><title>How it works</title><!-- paths from @hugocxl/vectors --></svg></div>
  <figcaption class="p9-caption"><span class="p9-label">Fig. 01 / How it works</span></figcaption>
</figure>
```
<!-- /specimen -->

### `figure-grid`

Two to four [vectors](#vectors) separated by hairlines. Each has a `Fig 0.N` label, a title of up to four words and one sentence. Set `data-columns` to the item count. The grid stacks when its container is narrower than 34rem.

<!-- specimen:figure-grid -->
```html
<ul class="p9-grid p9-wide" data-columns="3">
  <li>
    <span class="p9-label">Fig 0.1</span>
    <svg class="p9-vector" data-vector="modular-design" viewBox="0 0 480 360" role="img" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"><title>Modular design</title><!-- paths from @hugocxl/vectors --></svg>
    <h3>Purpose-built</h3>
    <p>Shaped by the practices of teams who ship daily.</p>
  </li>
  <li>
    <span class="p9-label">Fig 0.2</span>
    <svg class="p9-vector" data-vector="handoff" viewBox="0 0 480 360" role="img" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"><title>Handoff</title><!-- paths from @hugocxl/vectors --></svg>
    <h3>Shared by people and agents</h3>
    <p>From the first draft to the merged change.</p>
  </li>
  <li>
    <span class="p9-label">Fig 0.3</span>
    <svg class="p9-vector" data-vector="fast-performance" viewBox="0 0 480 360" role="img" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"><title>Fast performance</title><!-- paths from @hugocxl/vectors --></svg>
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
<ol class="p9-index">
  <li><span class="p9-label"><time datetime="2026-11-12">12 Nov 2026</time></span><div><h3>Persistent sessions</h3><p>Sessions survive restarts and reconnect where you left them.</p></div></li>
  <li><span class="p9-label"><time datetime="2026-10-28">28 Oct 2026</time></span><div><h3>Remote hosts</h3><p>Connect to any machine running the server.</p></div></li>
</ol>
```
<!-- /specimen -->

### `table`

Comparisons and specifications. Column headings use `scope="col"` and row headings use `scope="row"`. Always wrap the table in `.p9-table-scroll` with `tabindex="0"` so it can be scrolled by keyboard.

<!-- specimen:table -->
```html
<div class="p9-table-scroll" tabindex="0">
  <table class="p9-table">
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
<a class="p9-button" href="/download">Download for macOS</a>
```
<!-- /specimen -->

### `form`

A visible label, an underlined input with an icon submit button (`corner-down-left` to send or `arrow-right` to go, with an `aria-label`), optional help text and a live feedback line.

| State | Result |
| --- | --- |
| Idle | Placeholder in `faint`, feedback empty |
| Invalid submit | Value kept, `aria-invalid="true"` on the input, the fix written in the feedback line |
| Editing after an error | `aria-invalid` removed, feedback cleared |
| Pending | Submit disabled, feedback reads “Sending…” |
| Success | Feedback confirms in one sentence. Focus stays on the input. |
| Failure | Value kept, feedback explains the failure and how to retry |

<!-- specimen:form -->
```html
<form class="p9-form" action="/waitlist" method="post">
  <label for="waitlist-email">Sign up to secure your place in the waitlist</label>
  <div class="p9-input">
    <input type="email" id="waitlist-email" name="email" placeholder="you@example.com" required autocomplete="email" aria-describedby="waitlist-help waitlist-feedback">
    <button type="submit" aria-label="Join the waitlist"><svg class="p9-icon" data-icon="corner-down-left" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg></button>
  </div>
  <p class="p9-help" id="waitlist-help">We’ll let you know when the beta is available.</p>
  <output class="p9-feedback" id="waitlist-feedback" aria-live="polite"></output>
</form>
```
<!-- /specimen -->

### `code`

A command or snippet on the surface with a Copy button. `system/p9.js` handles the copy. `tabindex="0"` on `pre` keeps long lines scrollable by keyboard.

<!-- specimen:code -->
```html
<div class="p9-code"><pre tabindex="0"><code>brew install fieldwork</code></pre><button type="button">Copy</button></div>
```
<!-- /specimen -->

### `footer`

Mono links at both ends with a hairline between them. It is the last element in the body, after `</main>`.

<!-- specimen:footer -->
```html
<footer class="p9-footer">
  <ul><li><a href="/press">Press kit</a></li></ul>
  <ul><li><a href="/privacy">Privacy</a></li><li><a href="https://x.com/fieldwork">@fieldwork</a></li></ul>
</footer>
```
<!-- /specimen -->

## Icons and vectors

Pages draw with two companion libraries and nothing else. [`@hugocxl/icons`](https://hugocxl.github.io/icons/) label actions and [`@hugocxl/vectors`](https://hugocxl.github.io/vectors/) illustrate ideas. Both draw in `currentColor`, so they follow the theme and never touch the accent. No other icon set, illustration, emoji or symbol character may stand in for them.

```sh
npm install @hugocxl/design-system @hugocxl/icons @hugocxl/vectors
```

In the markup above, `<!-- paths from @hugocxl/icons -->` and `<!-- paths from @hugocxl/vectors -->` mark where the SVG's own content goes. Copy it from the package: the JavaScript export of each name is the SVG as a string, and the React components render it directly.

### Icons

Use the **Stroke** style. An icon either goes before the words of a link, the `button` or a `meta` label, or it is the whole content of an icon button that has an `aria-label`. Give the SVG `class="p9-icon"` and `data-icon` with its name: it sizes to `1em`, takes the text color and keeps `space-2` before the words. Inside an icon button the gap is removed.

```html
<!-- Before words -->
<a href="/docs"><svg class="p9-icon" data-icon="book-open" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg>Read the guide</a>
<a class="p9-button" href="/browse"><svg class="p9-icon" data-icon="search" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg>Browse icons</a>
<li class="p9-label"><svg class="p9-icon" data-icon="calendar" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg><time datetime="2026-11-18">18 November 2026</time></li>

<!-- Alone, in an icon button -->
<button class="p9-theme" type="button" data-p9-theme aria-label="Switch theme"><svg class="p9-icon" data-icon="contrast" viewBox="0 0 16 16" fill="none" aria-hidden="true"><!-- paths from @hugocxl/icons --></svg></button>
```

```jsx
import { BookOpenIcon } from '@hugocxl/icons/react/stroke';

<a href="/docs"><BookOpenIcon className="p9-icon" />Read the guide</a>
```

| Place | Icon |
| --- | --- |
| Theme button | `contrast` |
| Pager | `arrow-left`, `arrow-right` |
| Form submit | `corner-down-left` to send, `arrow-right` to go |
| Search | `search` |
| External link | `arrow-up-right` |

- One icon per element. Before words it never replaces a word; alone it needs an `aria-label`.
- Only in links, the button, meta labels and icon buttons. Never in headings, the statement, body sentences or the footer.
- Icons carry `aria-hidden="true"`. The React components add it unless they receive an `aria-label`.
- Never in the accent color, and never draw arrows, ◐ or other symbols as text instead.

### Vectors

Every figure is a vector from `@hugocxl/vectors`. It fills `figure-wide` and each `figure-grid` item, drawn in ink on the surface at its own 4:3 proportions. Inline the SVG, replace its root `xmlns` attribute with `class="p9-vector"` and `data-vector` with its name, and remove its `color` attribute.

```html
<figure class="p9-wide">
  <div class="p9-media"><svg class="p9-vector" data-vector="modular-design" viewBox="0 0 480 360" role="img" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round"><title>Modular design</title><!-- paths from @hugocxl/vectors --></svg></div>
  <figcaption class="p9-caption"><span class="p9-label">Fig. 02 / Modular design</span></figcaption>
</figure>
```

```jsx
import { ModularDesignVector } from '@hugocxl/vectors/react/modular-design';

<div className="p9-media"><ModularDesignVector className="p9-vector" /></div>
```

- Choose a vector for what it means. The [vectors browser](https://hugocxl.github.io/vectors/browse.html) lists all 2,000 by use case. Name it in the caption.
- Keep the SVG's `title` and `desc`: they are its accessible name.
- Use an `<img>` only for a screenshot of the product itself.
- Never crop a vector, color it with the accent or place it on the field.

## Do's and Don'ts

### Always

- Load `system/p9.css` and `system/theme.js` in the head and `system/p9.js` as a module.
- Set `class="p9"` and the recipe's `data-layout` on the body.
- Follow the recipe's component order. Copy component markup exactly and change only text, links, vector and icon names and IDs.
- Write in sentence case. Keep the title to one line and the statement to one sentence.
- Put supporting sentences in `.p9-muted`, inline after the main thought. Text on `surface` is always `ink`, because muted falls below 4.5:1 there.
- Keep every vector's `title`, give every icon button an `aria-label`, every image `alt` text and every field a visible label.
- Check the page at 320, 760, 761 and 1440px wide in both themes.

### Never

- Never add a class, color, font, size, weight, radius or spacing value that is not a token.
- Never use the accent more than twice, or on body text, links, buttons, backgrounds, rules or figures.
- Never set text larger than the title or bolder than 500 (the wordmark is the exception).
- Never use shadows, gradients, emoji, stock photography, symbol characters as icons, or icons and illustrations from outside `@hugocxl/icons` and `@hugocxl/vectors`.
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

`npm test` lints this file, checks that its markup matches the specimens, and runs browser tests on the reference: computed tokens in both themes, column and figure geometry at 320, 760, 761 and 1440px, the accent budget, keyboard behavior and an axe WCAG 2.2 AA scan. For a generated page, check the same things plus the recipe order. To compare screenshots, fix the browser, viewport, scale, theme, locale and motion settings, and wait for fonts and figures to load.
