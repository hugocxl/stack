"""Verify SVG construction, and list visual near-duplicates for review."""
from argparse import ArgumentParser
from hashlib import sha256
from itertools import combinations
from math import ceil, hypot
from pathlib import Path
import re
from xml.etree import ElementTree as XML

SVG = "{http://www.w3.org/2000/svg}"
PAIR = re.compile(r"(-?\d+\.\d{2}),(-?\d+\.\d{2})")
OPACITIES = {".34", ".43", ".76", "1"}
ROOT = Path(__file__).resolve().parents[1]


def fingerprint(strokes):
    """Rasterize the contours into a small bitmask without external render dependencies."""
    grid = 40
    points = [point for stroke in strokes for point in stroke]
    min_x, min_y = map(min, zip(*points))
    max_x, max_y = map(max, zip(*points))
    scale = (grid-5) / max(max_x-min_x, max_y-min_y)
    offset_x = (grid-1-(max_x-min_x)*scale)/2
    offset_y = (grid-1-(max_y-min_y)*scale)/2
    mask = 0
    for stroke in strokes:
        for (x,y),(a,b) in zip(stroke, stroke[1:]):
            steps = ceil(hypot(a-x,b-y)*scale*2) or 1
            for i in range(steps+1):
                u = round((x+(a-x)*i/steps-min_x)*scale+offset_x)
                v = round((y+(b-y)*i/steps-min_y)*scale+offset_y)
                mask |= 1 << (v*grid+u)
    return mask


def inspect(file):
    root = XML.parse(file).getroot()
    assert root.tag == SVG+"svg", "root must be SVG"
    assert root.get("viewBox") == "0 0 480 360" and root.get("fill") == "none", "invalid canvas"
    assert set(root.attrib) == {
        "viewBox", "role", "color", "fill", "stroke", "stroke-width", "stroke-linecap", "stroke-linejoin"
    }, "unexpected SVG attribute"
    assert root.get("stroke") == "currentColor", "outline color must be configurable"
    title, description, *paths = root
    assert title.tag == SVG+"title" and title.text, "title missing"
    assert description.tag == SVG+"desc" and description.text, "description missing"
    assert 1 <= len(paths) <= 4, "unexpected number of ink layers"

    strokes = []
    for path in paths:
        assert path.tag == SVG+"path" and not list(path), "unexpected SVG element"
        assert set(path.attrib) == {"vector-effect", "stroke-opacity", "d"}, "unexpected path attribute"
        assert path.get("stroke-opacity") in OPACITIES, "invalid ink layer"
        assert path.get("vector-effect") == "non-scaling-stroke", "invalid stroke scaling"
        commands = path.attrib["d"].split("M")
        assert not commands[0] and len(commands)>1, "missing move-to"
        for command in commands[1:]:
            pairs = command.split()
            assert len(pairs)>=2 and all(PAIR.fullmatch(pair) for pair in pairs), "invalid path coordinates"
            points = [tuple(map(float,p.split(","))) for p in pairs]
            assert all(30<=x<=450 and 35<=y<=325 for x,y in points), "clipped or off-center artwork"
            assert len(set(points))>1, "empty segment"
            strokes.append(points)

    signature = sha256("|".join(path.attrib["d"] for path in paths).encode()).digest()
    mask = fingerprint(strokes)
    assert mask.bit_count() >= 32, "insufficient visible geometry at small size"
    return signature, mask


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--expect", type=int)
    parser.add_argument("--similarity", type=float, default=.89, help="Report contour pairs above this similarity.")
    args = parser.parse_args()
    files = sorted((ROOT/"figures").glob("*.svg"))
    if args.expect is not None and len(files)!=args.expect:
        raise SystemExit(f"Expected {args.expect} SVGs, found {len(files)}")
    signatures = {}
    masks = []
    errors = []
    for file in files:
        try:
            signature, mask = inspect(file)
            if signature in signatures:
                raise ValueError(f"exact duplicate of {signatures[signature]}")
            signatures[signature] = file.stem
            masks.append((file.stem, mask))
        except (AssertionError, ValueError, XML.ParseError) as error:
            errors.append(f"{file.name}: {error}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Verified {len(files)} standalone SVGs with distinct geometry.")
    near = []
    for (name_a, a), (name_b, b) in combinations(masks, 2):
        score = (a&b).bit_count()/(a|b).bit_count()
        if score>=args.similarity:
            near.append((score,name_a,name_b))
    for score, a, b in sorted(near,reverse=True):
        print(f"Review {score:.0%} similar: {a} / {b}")
    print(f"{len(near)} pairs flagged for visual review.")


if __name__ == "__main__":
    main()
