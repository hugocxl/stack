from shapely.geometry import MultiPoint, Polygon

from geometry import BOLD, DETAIL, EDGE, oval, project, rounded
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A blood pressure monitor connected to a rolled arm cuff shows a paired reading above two stored entries."


def draw(s):
    rear = front_surface(s, angle=-30, y=-24)
    cuff = front_surface(s, angle=-30)
    outer = oval(-19, 22, 22, 22)
    inner = oval(-19, 22, 16.5, 16.5)
    body = MultiPoint([project(side.at(*p)) for side in (rear, cuff) for p in outer]).convex_hull
    hole = [Polygon([project(side.at(*p)) for p in inner]) for side in (rear, cuff)]
    s.layers.append((body.boundary, body.difference(hole[0].intersection(hole[1])), EDGE))
    cuff.line(outer, EDGE)
    cuff.line(inner, DETAIL)
    cuff.line([(-30, 37), (-33, 28), (-33, 17), (-29, 10)], DETAIL, dashed=True)
    s.tube([cuff.at(-14, 3), (-11, 13, 4), (-5, 18, 4),
            (3, 16, 4), (12, 11, 7), (18, 8, 10)], 1.9, EDGE)

    face = front_surface(s, angle=-21, y=12, z=8, lean=.46)
    face.slab(rounded(10, 0, 58, 54, 7), 8)
    face.frame(16, 13, 46, 35, 3, EDGE)
    face.line([(22, 35), (28, 35), (30, 40), (33, 31), (36, 35)], EDGE)
    face.rows(42, 41, (12,), ink=BOLD)
    face.rows(41, 35, (15,), ink=DETAIL)
    face.rows(42, 29, (10,), ink=BOLD)
    for z in (18, 23):
        face.rows(22, z, (9,))
        face.rows(42, z, (13,))
    face.oval(39, 7, 4, 2.2, EDGE)
