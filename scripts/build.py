"""Write the standalone SVG library and its gallery."""
from html import escape
from pathlib import Path
import argparse
import re

from geometry import Scene, paths_for
from scenes import product, workflow, infrastructure, data, control

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = [
    ("Product", product.FIGURES),
    ("Workflow", workflow.FIGURES),
    ("Infrastructure", infrastructure.FIGURES),
    ("Data", data.FIGURES),
    ("Trust & control", control.FIGURES),
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
    expected = set(files)
    if len(expected) != 50:
        raise ValueError(f"Expected 50 figures, found {len(expected)}")
    extra = {f.relative_to(ROOT).as_posix() for f in (ROOT/"figures").glob("*.svg")} - expected
    if extra:
        raise ValueError(f"Unexpected figures: {', '.join(sorted(extra))}")
    template = (ROOT/"scripts/gallery.html").read_text(encoding="utf-8")
    files["index.html"] = template.replace("<!-- COLLECTIONS -->", "\n".join(sections)).replace("<!-- CATEGORIES -->", "\n".join(links))
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
    print(f"{'Verified' if args.check else 'Built'} {len(expected)} static SVGs and the gallery.")


if __name__ == "__main__":
    main()
