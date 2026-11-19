from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project, rounded
from scenes.redraws._kit import coin

DESCRIPTION = "A chip payment card overlaps the rim of a single coin."


def card_face(s):
    """Draw a payment-size card in a shallow tilt and return its face mapping."""
    def point(x, y):
        return x, y, 5 + (58 - y) * .43

    outline = [point(x, y) for x, y in rounded(0, 0, 94, 58, 6)]
    bottom = [(x, y, z - 5) for x, y, z in outline]
    # Draw the silhouette of the extruded card, leaving its upper face crisp.
    hull = MultiPoint([project(p) for p in outline + bottom]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.face(outline, EDGE)
    return point


def chip_card(s):
    point = card_face(s)
    chip = rounded(12, 12, 24, 19, 4)
    s.line([point(x, y) for x, y in chip + chip[:1]], EDGE)
    for y in (18, 24):
        for x in (12, 29):
            s.line([point(x, y), point(x + 7, y)], DETAIL)
    s.line([point(24, 12), point(24, 31)], DETAIL)
    for x, y, width in ((13, 43, 35), (13, 49, 22), (68, 44, 13)):
        s.line([point(x, y), point(x + width, y)], DETAIL)


def draw(s):
    x, z = 102, 11
    y = coin(s, x, 38, z, 19, depth=4)
    s.line([(a, y, b) for a, b in oval(x, z, 13, 13, count=32)], DETAIL)
    chip_card(s)
