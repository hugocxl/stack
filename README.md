# P9 Figures

2,000 static isometric SVG illustrations for website heroes, feature sections, documentation, product states, and industry pages.

[Browse the gallery](https://hugocxl.github.io/p9-figures/) · [Search the use-case catalog](https://hugocxl.github.io/p9-figures/use-cases.html) · [Download the SVG files](figures/)

| Modular design | Product architecture | Fast performance |
| :---: | :---: | :---: |
| [![Four independent modules on a common footprint](figures/modular-design.svg)](figures/modular-design.svg) | [![An exploded stack with a raised top layer](figures/product-architecture.svg)](figures/product-architecture.svg) | [![A pulse rising through a bank of fins](figures/fast-performance.svg)](figures/fast-performance.svg) |

## Collections

- **Product** covers architecture, performance, responsive design, customization, integrations, and extensibility.
- **Workflow** covers collaboration, automation, planning, scheduling, search, and publishing.
- **Infrastructure** covers cloud services, storage, backups, load balancing, failover, and bandwidth.
- **Data** covers analytics, growth, forecasting, monitoring, and experiments.
- **Trust & control** covers security, permissions, privacy, approvals, recovery, and feature flags.
- **Product states** covers empty workspaces, missing pages, maintenance, and confirmations.
- **Commerce** covers checkout, fulfillment, receipts, returns, and product comparison.
- **Editorial & media** covers documentation, video, photography, newsletters, and learning.

The [illustration manifest](catalog/manifest.json) lists every SVG by use case, including where it can appear on a site. The [design review](DESIGN.md) documents the acceptance criteria and what the automated checks cover.

## Use an SVG

Copy any SVG from `figures/` into your project and reference it as an image. Every figure uses a transparent 480 × 360 viewBox and includes a title and description.

```html
<img src="/images/modular-design.svg"
     alt="Four independent modules fit into one assembly"
     width="480" height="360">
```

To recolor a file, edit the root `color` attribute. For inline SVG, override its `color` with CSS. The separate stroke opacities preserve the hierarchy between highlights, contours, and construction lines.

## Build from source

The assets, gallery, and use-case page are checked in. To regenerate them, use Python 3.10–3.13 in a virtual environment.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/build.py --expect 2000
python scripts/build.py --check --expect 2000
python scripts/verify.py --expect 2000 --similarity .965
```

The scene definitions live in `scripts/scenes/`. The build projects their 3D coordinates into SVG and removes hidden lines so the backdrop stays transparent. Open `index.html` to browse the gallery locally.

## License

The artwork and source are [MIT licensed](LICENSE). The figure design draws on the visual rules in [Hairline by Lucas Marques](https://hairline.lucasmarkes.com/skills).
