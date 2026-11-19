from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._w4 import bezier_path

DESCRIPTION = "A finned rocket lifts off with a compact flame below its nozzle."


def draw(s):
    # The nozzle and plume sit behind the near fins and fuselage.
    flame = bezier_path((-9, 27), ((-15, 15), (-6, 7), (0, 0)),
                        ((3, 8), (15, 15), (9, 27)))
    s.face([(x, 0, z) for x, z in [*flame, (-9, 27)]], EDGE)
    s.line([(-3, 0, 22), (-4, 0, 16), (0, 0, 10), (4, 0, 17)], DETAIL)
    s.solid(oval(0, 0, 10, 10)[:-1], 25, 8, top=oval(0, 0, 8, 8)[:-1])

    rings = ((33, 9), (39, 13), (55, 17), (72, 17), (86, 13), (97, 7), (105, 0))
    hull = MultiPoint([project((x, y, z)) for z, r in rings for x, y in oval(0, 0, r, r)]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.ellipse(0, 0, 41, 13.5, 13.5, DETAIL, start=-45, end=135)
    s.ellipse(0, 0, 83, 14.1, 14.1, EDGE, start=-45, end=135)
    s.line([(12 + .7*u, 12 - .7*u, z) for u, z in oval(0, 69, 7, 8)], EDGE)
    s.line([(12 + .7*u, 12 - .7*u, z) for u, z in oval(0, 69, 4.6, 5.4)], DETAIL)
    s.face([(10, 5, 54), (28, 5, 39), (29, 5, 25), (10, 5, 34)])
    s.face([(-4, 13, 52), (-4, 28, 37), (-4, 29, 26), (-4, 12, 33)])
