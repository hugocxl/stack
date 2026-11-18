# P9DS

[Open the P9DS guide](https://hugocxl.github.io/p9ds/). It contains the visual reference, interactive specimens, page composition rules, and agent handoff in one article.

Use [DESIGN.md](DESIGN.md) with a coding agent. Pin the revision and give it the page type, ordered sections, approved copy and assets, and action destinations. Use [index.html](index.html) as the reference markup.

## Use the system

Copy `system/` into your website. Load `system/cxl.css`, then `system/editorial.css`. Apply `cxl-editorial` to the body and wrap the content in an article with `cxl-reading cxl-opening` inside `main`. Include `system/theme.js` in the head to follow the system appearance and remember the visitor’s choice.

The base stylesheet provides the palette, bundled Geist typefaces, and control styles. The editorial stylesheet defines the reading column, right-edge texture, and wide figures. Use the classes `cxl-button`, `cxl-field`, and `cxl-label` for controls and captions, and `cxl-wide-figure` for illustrations that need the full width.

```js
import { keyboard } from './system/figures/index.js';
const figure = keyboard(document.querySelector('.illustration'));
// Release the figure when removing its container.
figure.destroy();
```

## Assets and influences

- Self-hosted WOFF2 fonts from [Vercel Geist](https://vercel.com/font), npm release 1.9.2. See [font license](system/fonts/Geist-LICENSE.txt).
- Interactive figures from [Hairline](https://github.com/lucasmarkes/hairline), version 0.5.1. The bundled vanilla module includes all 33 library figures with grayscale colors for both modes. See [figure license](system/figures/LICENSE).
- The dark palette comes from [Apollo](https://heyapollo.dev/), with a P9DS light adaptation. The textured margin and centered measure draw on [Superlogical](https://www.superlogical.com/) and its [public testing article](https://www.superlogical.com/updates/public-testing-beginning). P9DS’s artwork is bundled in `system/images/`.

## Development

Run `python3 -m http.server 8000` and open `http://localhost:8000`. GitHub Pages publishes the root of main.

Run `npm ci`, `npx playwright install chromium`, and `npm test` to lint the design file and check the reference in the browser. Update DESIGN.md and the shared CSS together when tokens change.
