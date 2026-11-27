"""Write the standalone SVG library and the use-case manifest."""
from html import escape
from pathlib import Path
import argparse
import json
import re

import geometry
from geometry import STROKE, Scene, paths_for
from scenes import commerce, control, data, editorial, infrastructure, new_states, product, workflow
from expansion import attach_artwork, packs
from scenes.redraws import REDRAWS

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


FALLBACKS = []


def render_svg(draw, title, description):
    """Draw with continuous corners. A few scenes splice an outline into a corner arc, so
    they keep circular corners where the longer squircle reach would cross the splice."""
    for continuous in (True, False):
        geometry.CONTINUOUS[0] = continuous
        try:
            scene = Scene()
            draw(scene)
            paths = paths_for(scene)
            break
        except Exception:
            if not continuous:
                raise
            FALLBACKS.append(title)
        finally:
            geometry.CONTINUOUS[0] = True
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" color="#8792a2" fill="none" stroke="currentColor" stroke-width="{STROKE}" stroke-linecap="round" stroke-linejoin="round">
  <title>{escape(title)}</title>
  <desc>{escape(description)}</desc>
{paths}
</svg>
'''


def validate_catalog(available, catalog):
    """Every use case has a unique ID and every published figure belongs to exactly one use case."""
    seen_ids, linked_assets = set(), set()
    for group in catalog["groups"]:
        for case in group["cases"]:
            identifier = case["id"]
            if identifier in seen_ids or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier):
                raise ValueError(f"Invalid or repeated use-case ID {identifier}")
            seen_ids.add(identifier)
            asset = case.get("asset")
            if asset:
                if asset not in available or asset in linked_assets:
                    raise ValueError(f"Unknown or repeated asset for {identifier}: {asset}")
                linked_assets.add(asset)
    if missing := available - linked_assets:
        raise ValueError(f"Figures missing from the use-case catalog: {', '.join(sorted(missing))}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check that the committed output is current.")
    parser.add_argument("--expect", type=int, help="Require exactly this many published SVGs.")
    args = parser.parse_args()
    files = {}
    for _, figures in COLLECTIONS:
        for draw, title, description in figures:
            file = f"figures/{slug(title)}.svg"
            if file in files:
                raise ValueError(f"Duplicate figure {file}")
            draw, description = REDRAWS.get(slug(title), (draw, description))
            files[file] = render_svg(draw, title, description)
    catalog = json.loads((ROOT/"catalog/use-cases.json").read_text(encoding="utf-8"))
    expansion = [
        (group, identifier, title, placement, *REDRAWS.get(identifier, (draw, visual))[::-1])
        for group, identifier, title, placement, visual, draw in packs()
    ]
    attach_artwork(catalog, expansion)
    for group in catalog["groups"]:
        group_entries = [entry for entry in expansion if entry[0] == group["id"]]
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
    expected = set(files)
    if args.expect is not None and args.expect != len(expected):
        raise SystemExit(f"Expected {args.expect} published figures, found {len(expected)}")
    extra = {f.relative_to(ROOT).as_posix() for f in (ROOT/"figures").glob("*.svg")} - expected
    if extra:
        raise ValueError(f"Unexpected figures: {', '.join(sorted(extra))}")
    validate_catalog(expected, catalog)
    files["catalog/manifest.json"] = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    stale = []
    for relative, content in files.items():
        path = ROOT/relative
        if args.check:
            if not path.exists() or not same_output(path.read_text(encoding="utf-8"), content):
                stale.append(relative)
        else:
            path.parent.mkdir(exist_ok=True, parents=True)
            path.write_text(content, encoding="utf-8")
    if stale:
        raise SystemExit("Regenerate these files with python scripts/build.py:\n" + "\n".join(stale))
    print(f"{'Verified' if args.check else 'Built'} {len(expected)} static SVGs and the use-case manifest.")
    if not args.check:
        print("Run python3 scripts/generate.py to update the npm and Swift packages.")


NUMBER = re.compile(r"-?\d+(?:\.\d+)?")


def same_output(committed, built):
    """Floating-point rounding can move a coordinate by 0.01 between platforms. Accept that, and nothing else."""
    if committed == built:
        return True
    if NUMBER.sub("#", committed) != NUMBER.sub("#", built):
        return False
    return all(abs(float(a) - float(b)) <= 0.0101 for a, b in zip(NUMBER.findall(committed), NUMBER.findall(built)))


if __name__ == "__main__":
    main()
