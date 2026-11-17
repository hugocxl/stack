# IconsCXL website

Run `npm ci` and `npm run build:site`. Serve `_site` with any static HTTP server.
Run `node scripts/check-site.mjs` to check navigation, guide anchors, and assets.

`scripts/build-site.mjs` builds the landing page from the actual SVG artwork and
renders `docs/USAGE.md` into the platform guide. `scripts/gallery.html` is the
source for the full offline icon browser; run `npm run generate` after changing
it. The site includes that generated browser as `icons.html`.

The visual language follows the Tab website: Junicode headings, warm paper,
brown accents, thin rules, and system UI body text. The bundled Junicode font
is distributed under its included OFL license.

`.github/workflows/pages.yml` builds, checks, and deploys the site on main.
Only `_site` is published; package sources and internal review files stay out
of the Pages artifact.
