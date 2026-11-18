# Icons website

The site at https://hugocxl.github.io/icons/ is built strictly from the P9 design
system shared by the @hugocxl stack (Icons, Vectors, Design system).

```sh
npm ci
npm run build:site              # website/ → _site/
node scripts/check-site.mjs     # links, anchors, assets and the P9 page contract
node --test tests/gallery.test.mjs
```

Serve `_site` with any static HTTP server.

- `system/` is the design system, copied verbatim from `../design-system/system/`
  by `npm run sync:design-system` (`-- --check` reports drift). It is committed
  because CI has no sibling checkout. Never edit it here.
- `index.html` (recipe `home`), `browse.html` (layout `plain`) and `docs.html`
  (recipe `docs`) are templates. `scripts/build-site.mjs` fills in `{{…}}` values
  from `catalog.json` and `packages/icons/package.json`, inlines real artwork and
  renders `docs/USAGE.md` into the docs page. `partials/` holds the shared head,
  masthead and footer.
- `site.css` holds the only site-specific styles. It may use `--ds-*` properties
  and the documented spacing and radius tokens only; `check-site.mjs` enforces it.
- `browse.js` is the icon browser. The build copies every SVG to
  `svg/<style>/<name>.svg`; the browser fetches each file only when its cell
  nears the viewport. `#name` deep-links to an icon's detail view.
- `home.js` cycles the home specimen through Duotone, Solid and Stroke.

`.github/workflows/pages.yml` builds, checks and deploys `_site` on main.
