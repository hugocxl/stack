from shapely.geometry import MultiPoint, Polygon

from geometry import DETAIL, EDGE, oval, project, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w4 import Surface

DESCRIPTION = "A smartwatch shows a crescent moon above a stepped overnight sleep timeline."


def smartwatch(s):
    """Set a rounded smartwatch upright on its closed wristband."""
    outer = oval(-15, 33, 23, 33, count=64)
    inner = oval(-15, 33, 18, 27, count=64)
    far, near = -16, 16
    hull = MultiPoint([project((x, y, z)) for x in (far, near) for y, z in outer]).convex_hull
    opening = [
        Polygon([project((x, y, z)) for y, z in inner]) for x in (far, near)
    ]
    s.layers.append((hull.boundary, hull.difference(opening[0].intersection(opening[1])), EDGE))
    s.line([(near, y, z) for y, z in outer], EDGE)
    s.line([(near, y, z) for y, z in inner], DETAIL)
    s.box(22, 3, 32, 5, 8, 8, 2)

    screen = Surface(s, lambda u, v: (u, 13 - .09*(v - 16), v))
    screen.slab(rounded(-23, 10, 46, 47, 10), 6)
    screen.frame(-18, 15, 36, 37, 7, DETAIL)
    return screen


def draw(s):
    screen = smartwatch(s)
    glyph(s, "moon", *screen.at(-2, 40), 10)
    screen.line([(-13, 31), (-9, 31), (-9, 25), (-3, 25), (-3, 20),
                 (4, 20), (4, 27), (9, 27), (9, 31), (13, 31)], EDGE)
