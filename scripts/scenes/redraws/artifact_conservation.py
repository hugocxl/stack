from shapely.geometry import MultiPoint
from shapely.ops import unary_union

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._w3 import Surface

DESCRIPTION = "A fine conservation brush touches the shoulder of an antique vase."


def museum_vase(s, x=0, y=0, z=0, *, scale=1):
    """A wheel-thrown vase with a continuous profile, narrow foot and flared rim."""
    profile = [(10, 0), (11, 2), (11, 4), (9, 6), (10, 9), (12, 12),
               (15, 16), (18, 22), (20, 28), (21, 34), (21, 38), (20, 42),
               (18, 46), (14, 50), (9, 54), (7, 57), (7, 61), (8, 63),
               (11, 65), (11, 67)]
    rings = [[project((a, b, z + height * scale))
              for a, b in oval(x, y, radius * scale, radius * scale, count=40)]
             for radius, height in profile]
    hull = unary_union([MultiPoint(a + b).convex_hull for a, b in zip(rings, rings[1:])])
    s.layers.append((hull.boundary, hull, EDGE))
    s.ellipse(x, y, z + 67 * scale, 11 * scale, 11 * scale, EDGE)
    s.ellipse(x, y, z + 67 * scale, 7 * scale, 7 * scale)
    s.ellipse(x, y, z + 35 * scale, 20.8 * scale, 20.8 * scale, start=-45, end=135)


def draw(s):
    museum_vase(s)
    brush = Surface(s, (16, 13, 41))

    def along(u, v):
        return (.68 * u - .73 * v, .73 * u + .68 * v)

    grip = [(0, 0), (5, -3.5), (11, -4), (20, -3.5), (26, -2.5),
            (57, -1.5), (59, 0), (57, 1.5), (26, 2.5), (20, 3.5),
            (11, 4), (5, 3.5)]
    brush.plate([along(u, v) for u, v in grip], 2)
    for u, radius in ((11, 4), (20, 3.5)):
        brush.stroke([along(u, -radius), along(u, radius)], EDGE)
    brush.stroke([along(3, 0), along(9, .4)], DETAIL)
