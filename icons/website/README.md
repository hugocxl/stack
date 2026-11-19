# @hugocxl/icons website

The site at https://hugocxl.github.io/stack/icons/ is built strictly from the P9 design
system shared by the @hugocxl stack (@hugocxl/icons, @hugocxl/vectors, @hugocxl/design-system).

```sh
npm ci
npm run build:site              # website/ → _site/
node scripts/check-site.mjs     # links, anchors, assets and the P9 page contract
node --test tests/gallery.test.mjs
```

Serve `_site` with any static HTTP server.

- The design system comes from the `@hugocxl/design-system` devDependency: the
  build copies its `system/` folder to `_site/system/`. The Pages workflow
  installs `@hugocxl/design-system@latest` before building, so every deploy
  (including the ones a design-system release triggers) uses the newest release.
  The icons on the site come from this repository.
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
