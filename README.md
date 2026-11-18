# CXL Design System

[Open the living preview](https://hugocxl.github.io/cxl-design-system/).

Start with the [Interface Guidelines](https://hugocxl.github.io/cxl-design-system/#guidelines) when designing a page. The guidelines, examples, and setup live in one article.

Copy `system/` into a website. Link `system/cxl.css` and use its custom properties for page backgrounds, text, surfaces, borders, spacing and typography. Set `data-theme="light"` or `data-theme="dark"` on the HTML element. The preview follows the operating system until the visitor chooses a mode.

~~~css
body {
  background: var(--cxl-bg);
  color: var(--cxl-text);
  font-family: var(--cxl-sans);
}
~~~

Geist Sans carries all prose, headings, and controls. Geist Mono marks code and technical notes. The editorial layout uses fluid prose (about 21 px at 1440 px) with 1.3 line height, a centered 60ch reading column, and paragraph spacing for changes of subject. Load `system/editorial.css` after the base stylesheet and apply `cxl-reading` to the article. Place a figure with the `cxl-wide-figure` class inside the reading column to extend it to the article gutters. The preview keeps a semantic page title available to screen readers.

Use the classes cxl-button, cxl-field and cxl-label for controls and captions. Mount a bundled interactive figure into a sized container from a module script.

~~~js
import { keyboard } from './system/figures/index.js';
const figure = keyboard(document.querySelector('.illustration'));
// When removing the container
figure.destroy();
~~~

## Assets and influences

- Self-hosted WOFF2 fonts from [Vercel Geist](https://vercel.com/font), npm release 1.9.2. See system/fonts/Geist-LICENSE.txt.
- Interactive figures from [Hairline](https://github.com/lucasmarkes/hairline), version 0.5.1. The bundled vanilla module includes all 33 library figures with grayscale colors for both modes. See system/figures/LICENSE.
- The dark palette comes from [Apollo](https://heyapollo.dev/), with a CXL light adaptation. The long paragraphs and fixed textured margin draw on [Superlogical](https://www.superlogical.com/). The centered measure and early wide illustration follow the [public testing article](https://www.superlogical.com/updates/public-testing-beginning). CXL’s grayscale artwork is bundled in `system/images/`.

## Development

Serve the repository with `python3 -m http.server 8000` and open localhost:8000. The preview uses the same system folder as consumers. GitHub Pages publishes the root of main.
