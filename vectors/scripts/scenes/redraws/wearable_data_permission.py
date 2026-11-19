from shapely.geometry import MultiPoint, Polygon

from geometry import BOLD, DETAIL, EDGE, oval, project, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface

DESCRIPTION = "A smartwatch shows a pulse trace on its screen and carries a lock badge."


def draw(s):
    # The closed wristband supports the watch on the floor.
    outer = oval(-15, 33, 23, 33, count=64)
    inner = oval(-15, 33, 19, 28, count=64)
    far, near = -16, 16
    hull = MultiPoint([project((x, y, z)) for x in (far, near) for y, z in outer]).convex_hull
    opening = Polygon([project((near, y, z)) for y, z in inner])
    rear_opening = Polygon([project((far, y, z)) for y, z in inner])
    s.layers.append((hull.boundary, hull.difference(opening.intersection(rear_opening)), EDGE))
    s.line([(near, y, z) for y, z in outer], EDGE)
    s.line([(near, y, z) for y, z in inner], DETAIL)
    s.box(22, 3, 32, 5, 8, 8, 2)

    screen = Surface(s, lambda u, v: (u, 13 - .09*(v - 16), v))
    screen.slab(rounded(-23, 10, 46, 47, 10), 6)
    screen.frame(-18, 15, 36, 37, 7, DETAIL)
    screen.line([(-14, 33), (-9, 33), (-6, 39), (-2, 26), (2, 43),
                 (6, 33), (14, 33)], BOLD)
    badge(s, "lock", *screen.at(20, 18), 14)
