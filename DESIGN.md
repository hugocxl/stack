---
version: alpha
name: P9DS
description: Editorial design system defined by the single-page P9DS reference.
colors:
  primary: "#0d0d0d"
  paper: "#fafafa"
  graphite: "#878787"
  ring: "#d4d4d8"
  light:
    surface: "#f2f2f2"
    muted: "#505050"
  dark:
    surface: "#131313"
    muted: "#808080"
    line: "#1d1d1d"
typography:
  reading:
    fontFamily: Geist Sans
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: -0.01em
  introduction:
    fontFamily: Geist Sans
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.02em
  control:
    fontFamily: Geist Sans
    fontSize: 14px
    fontWeight: 400
    letterSpacing: -0.01em
  emphasis:
    fontFamily: Geist Sans
    fontWeight: 600
  caption:
    fontFamily: Geist Mono
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.06em
rounded:
  control: 6px
  material: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  paragraph: 1.25rem
  section: 2.5rem
  target: 44px
components:
  button-light:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.paper}"
    typography: "{typography.control}"
    rounded: "{rounded.control}"
  button-dark:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.primary}"
    typography: "{typography.control}"
    rounded: "{rounded.control}"
  surface-light:
    backgroundColor: "{colors.light.surface}"
    textColor: "{colors.light.muted}"
  surface-dark:
    backgroundColor: "{colors.dark.surface}"
    textColor: "{colors.dark.muted}"
---
## Overview

The [P9DS reference](index.html) is the visual standard. Use its centered reading column, small muted headings, near-black and paper palette, side texture, and inline links. The same editorial shell serves product, documentation, and form pages. Read the [page composition rules](index.html#site-building) for their section order.

Define the audience, primary task, success condition, and relevant usage context before choosing a pattern. For the figure picker, success means a reader can find the named figure, preview it by keyboard, and identify the result. Test user tasks with representative people, including people with disabilities. Require an example and an observable result for each shared pattern. [GOV.UK design principles](https://www.gov.uk/guidance/government-design-principles) · [GOV.UK contribution criteria](https://design-system.service.gov.uk/community/contribution-criteria/)

### Source of truth

Pin a Git commit for the reference HTML, styles, and local assets. Load `system/cxl.css` first and `system/editorial.css` second. Use those stylesheets for rendered values and responsive behavior. Use the corresponding markup and scripts for component structure and behavior. The page brief supplies content, section order, and any approved component choices. Raise a discrepancy between the brief, the token file, and runtime code for review so the fix can land in the shared source.

The Google Labs draft organizes exact token values in YAML, usage in Markdown, and component references as `@path` pointers in prose. P9DS keeps the draft’s section order and uses the pinned `@google/design.md` 0.4.0 linter. The front matter describes the tokens implemented by the CSS. Check correspondence in the browser when changing either file. Typed JSON and the DTCG resolver are available for interchanging tokens and theme contexts with tools. Generate any export from the shared values. [Google Labs specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md) · [DTCG format and resolver](https://www.designtokens.org/tr/2025.10/)

A valid token file answers questions about values and roles. Include coded references for the rest of the design. In a 2026 corpus study, 47.5% of the 17,240 unique files had a Components heading without recognized component tokens. The study measures file structure and coverage. [DesignSpecs preprint](https://arxiv.org/html/2611.17713v1#S4.SS3)

## Colors

Use `--cxl-bg` for canvas, `--cxl-text` for text, `--cxl-muted` for supporting text, `--cxl-surface` for figures and snippets, and `--cxl-line` for fine rules. Light mode uses paper as canvas, primary ink as text, and ring for rules. Dark mode flips canvas and text and uses the dark rule value. Filled actions take the theme’s text color and use the canvas color for their label.

Resolve colors by role in each theme. The theme script follows the system until the visitor selects a mode, then applies that choice on later visits. Specify intended foreground and background pairs and check contrast in the rendered states. Use fine rules as decoration. When a boundary identifies a control, give it the non-text contrast required for that use. Use labels, shape, or other persistent cues alongside color to show state. [USWDS color roles](https://designsystem.digital.gov/design-tokens/color/overview/) · [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

## Typography

Use the bundled `Geist-Variable.woff2` for prose and controls and `GeistMono-Variable.woff2` for captions, dates, and code. Reading size is `min(calc(1rem + .36vw), 1.54rem)` with 1.3 line height. The opening uses `clamp(1.5rem, 1rem + 1vw, 2.75rem)` with 1.15 line height and a 44ch cap. Give section headings the reading size, weight 400, muted tone, and a 1rem bottom margin. Use weight 600 for emphasis. Allow copy and labels to wrap with their content intact.

## Layout

Use `body.cxl-editorial` with one `main` containing `.cxl-reading`. Center the reading column within the available main area and cap it at 60ch. Use 1.25rem after paragraphs and 2.5rem around sections. `.cxl-wide-figure` uses the available main width up to 1280px and keeps its caption beneath the figure.

Above 760 CSS pixels, use the `clamp(1.25rem, 5vw, 5rem)` gutter and reserve `clamp(15rem, 23vw, 34rem)` on the right for the fixed texture. At 760px and below, the reserved width is 20px, the texture is 12px wide, and the gutter is `clamp(1rem, 5vw, 2rem)`. The sidebar art is decorative. Keep the content’s reading and focus order across width changes. Check reflow at 320 CSS pixels and text resize to 200%.

For the guide, use a normal paragraph of inline links beneath the introduction to jump to sections. In other page types, choose the matching [page recipe](index.html#site-building), then supply the final section order. Include optional sections when the brief supplies eligible content. Omit the whole section when that content is absent.

## Elevation & Depth

Group content with whitespace and fine rules. Use a flat surface for figures and code. Reserve the shared material surface for compact groups of related controls.

## Shapes

Use the 6px field and button radius. Give icon controls a 44px target and use the shared pill shape for grouped controls.

## Motion & Micro-interaction

Keep the 2px focus outline with a 4px offset. Use the shared 120ms ease-out transition for compact controls and respect reduced motion and reduced transparency. Keep the meaning and controls of a figure available in a still state.

## Voice & Content Strategy

Use sentence case, a concise opening, and clear link labels. Put examples beside the claims they illustrate. Use approved assets and attribute evidence. Provide text or captions for meaningful images. Keep the action near its status and keep entered values through a validation error.

## Components

For each component, record its purpose, required markup and content slots, supported variants and their default, named token roles, and state transitions. For transitions, specify the trigger, visible result, retained values, focus destination, and accessible announcement where applicable. Give each meaningful state a fixed example or fixture. [GOV.UK text input](https://design-system.service.gov.uk/components/text-input/) · [W3C interaction patterns](https://www.w3.org/WAI/ARIA/apg/patterns/) · [Storybook state examples](https://storybook.js.org/docs/writing-stories)

- **Page shell and links** follow `@index.html` and `@system/editorial.css`. The shell controls the reading measure, space, and texture. Use underlined text for supporting links.
- **Primary action** uses `.cxl-button` from `@system/cxl.css`. Use an anchor with a destination for navigation and a button for an in-place action. Use one filled action per group. P9DS uses 14px Geist Sans at weight 400, 12px block and 18px inline padding, and a 6px radius. The theme determines its foreground and background. The shared hover and focus rules apply.
- **Field and feedback** follow `@index.html#components` and `@preview.js`. Include a visible label associated with the field ID, the input, and adjacent feedback. Associate feedback with the field and keep entered values when validation fails. For async actions, define idle, pending, success, and error. Show progress beside the action, prevent duplicate activation while pending, announce the result, and define retry. Specify an empty state where the task can return no content.
- **Figures and captions** use `.cxl-wide-figure` and `.cxl-label`. Give meaningful figures a text equivalent, and preserve the asset’s intended crop and reserved display dimensions. Use `.cxl-material.cxl-pager` for the named group of 44px arrow controls. Their order follows the figure’s reading direction and focus order.

### Figure picker

The reference uses the local figure catalog in `system/figures/index.js` and the chooser behavior in `preview.js`. It accepts Keyboard, Terrain, and Dish in that order. Input is trimmed and matched case-insensitively.

| State or action | Observable result |
| --- | --- |
| Initial | Keyboard is visible. The label reads “Find a figure”, the input is empty, and the feedback region is empty. |
| Previous or next | Advance to the corresponding figure, wrapping at either end. Update the caption and keep focus on the activated button. |
| Empty submission | The required field uses native browser validation. |
| Unknown name | Preserve the field value and current figure. Set `aria-invalid="true"` and announce “Choose Keyboard, Terrain, or Dish.” |
| Edit the field | Clear the previous error and status message. |
| Valid name | Update the figure and caption, announce “Showing” followed by its name, and move focus to “Next figure”. |

Bind an agent to the coded component whenever it exists. A visual reference helps review the result. Component names and exact markup give the agent an implementation to reuse. [Design2Code benchmark](https://aclanthology.org/2025.naacl-long.199/) · [Figma example of design-to-code mapping](https://developers.figma.com/docs/figma-mcp-server/code-connect-integration/)

## Do's and Don'ts

### Brief the agent

Explicitly direct the agent to read this file, the relevant reference markup, the shared CSS, and the component script at the pinned revision. In a consuming project, put that pointer in the task prompt or its agent instructions. Supply the user task, page type, ordered section IDs, variants, exact copy, real destinations, versioned assets with alt text or captions, and state fixtures. Specify which choices are fixed and which the agent may propose. Surface missing required inputs for a decision. Use the visual reference and classes as the defaults. [Agent instructions convention](https://agents.md/)

Here is an example brief as data for a downstream figure guide. The component names and IDs make the instructions unambiguous for a shared renderer.

```json
{
  "designRevision": "<P9DS commit SHA>",
  "template": "editorial",
  "task": "Find and preview a named figure by keyboard",
  "sections": [
    { "id": "opening", "type": "introduction", "text": "Explore the figures." },
    {
      "id": "components",
      "type": "figure-picker",
      "figures": ["keyboard", "terrain", "dish"],
      "initialFigure": "keyboard",
      "label": "Find a figure",
      "submitLabel": "Preview"
    }
  ],
  "fixtures": {
    "invalidQuery": "unknown",
    "validQuery": "terrain",
    "viewportWidths": [320, 760, 761, 1440],
    "themes": ["light", "dark"]
  }
}
```

### Repeatable generation

Treat model proposals as drafts. Identical prompts or sampling settings can yield different outputs. For a generator that must repeat a build, accept a page plan constrained to an allowlisted catalog of components, variants, and typed slots. Use a schema with required fields, enumerated IDs, and unknown fields rejected. Check that referenced assets exist, links resolve, section IDs are unique, and section order satisfies the chosen recipe. Retain the approved plan as an input. Feed it to a fixed, versioned renderer and shared CSS. Build from that plan and revision each time. [Research on inference variability](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) · [JSON Schema validation](https://json-schema.org/draft/2020-12/json-schema-validation) · [Agent and renderer catalog design](https://a2ui.org/concepts/catalogs/)

### Verify the result

Run `npm test` in P9DS to lint this document and exercise the reference. Its browser checks cover token values, loaded fonts, reflow, the texture breakpoint, figure search and focus, and both themes. For a consuming page, assert the required DOM order and component roles, computed styles, expected state transitions, and valid links. Check keyboard and screen-reader behavior with the intended task. Apply WCAG 2.2 AA to the rendered page and its complete interactions. [W3C accessibility evaluation](https://www.w3.org/WAI/test-evaluate/)

For pixel comparison, record the browser build and OS, viewport, device scale, browser theme, locale, time and data fixtures, and the animation state. Wait for the local fonts and images and keep the same reference environment for each baseline. To evaluate whether agents follow the brief, run several independent generations with fixed inputs and measure how many pass the same checks. [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots)
