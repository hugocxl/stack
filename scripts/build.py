"""Write the standalone SVG library and its gallery."""
from html import escape
from pathlib import Path
import argparse
import json
import re

from geometry import Scene, paths_for
from scenes import commerce, control, data, editorial, infrastructure, new_states, product, workflow
from catalog_page import render_catalog
from expansion import attach_artwork, packs

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = [
    ("Product", product.FIGURES),
    ("Workflow", workflow.FIGURES),
    ("Infrastructure", infrastructure.FIGURES),
    ("Data", data.FIGURES),
    ("Trust & control", control.FIGURES),
    ("Product states", new_states.FIGURES),
    ("Commerce", commerce.FIGURES),
    ("Editorial & media", editorial.FIGURES),
]


def slug(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def render_svg(draw, title, description):
    scene = Scene()
    draw(scene)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" color="#8792a2" fill="none" stroke="currentColor" stroke-width="1.05" stroke-linecap="round" stroke-linejoin="round">
  <title>{escape(title)}</title>
  <desc>{escape(description)}</desc>
{paths_for(scene)}
</svg>
'''


def card(file, title, description):
    title = escape(title)
    description = escape(description)
    return f'''<li class="card" data-figure>
  <a class="art" href="{file}" aria-label="Open {title} SVG"><img src="{file}" width="480" height="360" alt="" loading="lazy"></a>
  <div class="card-info"><div><h3><a href="{file}">{title}</a></h3><p>{description}</p></div>
  <a class="download" href="{file}" download aria-label="Download {title} SVG" title="Download SVG"><span aria-hidden="true">↓</span></a></div>
</li>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check that the committed output is current.")
    parser.add_argument("--expect", type=int, help="Require exactly this many published SVGs.")
    args = parser.parse_args()
    files, sections, links = {}, [], []
    for category, figures in COLLECTIONS:
        cards = []
        for draw, title, description in figures:
            file = f"figures/{slug(title)}.svg"
            if file in files:
                raise ValueError(f"Duplicate figure {file}")
            files[file] = render_svg(draw, title, description)
            cards.append(card(file, title, description))
        section_id = slug(category)
        label = escape(category)
        links.append(f'<a href="#{section_id}">{label}</a>')
        sections.append(f'<section id="{section_id}"><h2>{label}</h2><ul class="cards">\n' + "\n".join(cards) + "\n</ul></section>")
    catalog = json.loads((ROOT/"catalog/use-cases.json").read_text(encoding="utf-8"))
    expansion = list(packs())
    attach_artwork(catalog, expansion)
    for group in catalog["groups"]:
        group_entries = [entry for entry in expansion if entry[0] == group["id"]]
        if not group_entries:
            continue
        cards = []
        for _, identifier, title, _, description, draw in group_entries:
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier):
                raise ValueError(f"Invalid figure name {identifier}")
            file = f"figures/{identifier}.svg"
            if file in files:
                raise ValueError(f"Duplicate figure {file}")
            try:
                files[file] = render_svg(draw, title, description)
            except Exception as error:
                raise ValueError(f"Could not draw {file}") from error
            cards.append(card(file, title, description))
        section_id = group["id"]
        label = escape(group["title"])
        links.append(f'<a href="#{section_id}">{label}</a>')
        sections.append(f'<section id="{section_id}"><h2>{label}</h2><ul class="cards">\n' + "\n".join(cards) + "\n</ul></section>")
    expected = set(files)
    if args.expect is not None and args.expect != len(expected):
        raise SystemExit(f"Expected {args.expect} published figures, found {len(expected)}")
    extra = {f.relative_to(ROOT).as_posix() for f in (ROOT/"figures").glob("*.svg")} - expected
    if extra:
        raise ValueError(f"Unexpected figures: {', '.join(sorted(extra))}")
    template = (ROOT/"scripts/gallery.html").read_text(encoding="utf-8")
    files["index.html"] = (
        template.replace("<!-- COLLECTIONS -->", "\n".join(sections))
        .replace("<!-- CATEGORIES -->", "\n".join(links))
        .replace("{{figure_count}}", f"{len(expected):,}")
    )
    files["use-cases.html"] = render_catalog(ROOT, expected, catalog)
    files["catalog/manifest.json"] = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    stale = []
    for relative, content in files.items():
        path = ROOT/relative
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(relative)
        else:
            path.parent.mkdir(exist_ok=True, parents=True)
            path.write_text(content, encoding="utf-8")
    if stale:
        raise SystemExit("Regenerate these files with python scripts/build.py:\n" + "\n".join(stale))
    print(f"{'Verified' if args.check else 'Built'} {len(expected)} static SVGs, the gallery and use-case catalog.")


if __name__ == "__main__":
    main()
