# CXL Design System

[Open the living preview](https://hugocxl.github.io/cxl-design-system/).

Copy `system/` into a website. Link `system/cxl.css` and use its custom properties for page backgrounds, text, surfaces, borders, spacing and typography. Set `data-theme="light"` or `data-theme="dark"` on the HTML element. The preview follows the operating system until the visitor chooses a mode.

~~~css
body {
  background: var(--cxl-bg);
  color: var(--cxl-text);
  font-family: var(--cxl-sans);
}
h1 { font-family: var(--cxl-serif); }
~~~

The stylesheet applies Geist Sans to body text, controls and H3–H6, Geist Serif to H1 and H2, and Geist Mono to code and keyboard input. Use `.cxl-note` for technical notes. Give the primary action prominence with the ink fill. Use amber sparingly for emphasis. Build sections around one heading, generous whitespace and a thin dividing rule. Use the 4, 8, 16, 24, 40 and 64 px spacing scale. The preview stacks paired panels below 761 px.

Use the classes cxl-button, cxl-field and cxl-label for controls and captions. Mount a bundled interactive figure into a sized container from a module script.

~~~js
import { keyboard } from './system/figures/index.js';
const figure = keyboard(document.querySelector('.illustration'));
// When removing the container
figure.destroy();
~~~

## Assets and influences

- Self-hosted WOFF2 fonts from [Vercel Geist](https://vercel.com/font), npm release 1.9.2. See system/fonts/Geist-LICENSE.txt.
- Interactive figures from [Hairline](https://github.com/lucasmarkes/hairline), version 0.5.1. The bundled vanilla module includes all 33 library figures. See system/figures/LICENSE.
- The palette draws on [Superlogical](https://www.superlogical.com/). Landing-page hierarchy and composition take cues from [UserJot](https://userjot.com/) and [Studio Sphere](https://www.studiosphere.co/work).

## Development

Serve the repository with `python3 -m http.server 8000` and open localhost:8000. The preview uses the same system folder as consumers. GitHub Pages publishes the root of main.
