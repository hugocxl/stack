from shapely.geometry import MultiPoint

from geometry import BOLD, DETAIL, EDGE, oval, project
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import printed_stroke

DESCRIPTION = "An ingredient substitution arrow leads from a mushroom to a bell pepper."


def draw(s):
    # The gills sit under a domed cap on a short mushroom stalk.
    s.solid(oval(0, 0, 5.5, 5.5)[:-1], -3, 17, oval(0, 0, 4, 4)[:-1],
            crease=False)
    s.solid(oval(0, 0, 13.5, 13.5)[:-1], 10, 4,
            oval(0, 0, 15, 15)[:-1], crease=False)
    # A single convex side-and-cap envelope avoids seams across the dome.
    bands = [(14, 15), (18.4, 14.4), (22.3, 11.6), (25.2, 7.6), (26.6, 2.2)]
    hull = MultiPoint([project((x, y, z)) for z, r in bands for x, y in oval(0, 0, r, r)]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.ellipse(0, 0, 14, 15, 15, DETAIL, start=6, end=84)

    x = 46
    front = lambda u, z: (x + u, -2 + .12 * u, z + 9)
    body = [(-13, 17), (-12.5, 21), (-9, 24), (-5, 24.6), (-2.5, 23.5),
            (1, 25), (6, 25), (9, 23), (12, 21.7), (14, 18), (13.5, 12),
            (11.6, 6), (10, 2.5), (5.5, .5), (2, 1.3), (-1, 0), (-6, .6),
            (-9, 3), (-12, 8), (-13, 13)]
    s.face([(a, y - 9, z + 2) for a, y, z in (front(u, v) for u, v in body)])
    s.face([front(u, v) for u, v in body])
    printed_stroke(s, front, [(-5, 23), (-7, 17), (-6, 9), (-4, 3)], DETAIL)
    printed_stroke(s, front, [(7, 23), (8, 17), (7, 10), (5, 4)], DETAIL)
    s.tube([front(0, 23.5), front(-1, 27), front(1, 31), front(4, 31.5)], 1.4)

    arrow(s, [(15, -2, 14), (25, -4, 16), (29, -5, 17)], BOLD, head=5.8)
