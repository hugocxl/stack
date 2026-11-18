from math import cos, radians, sin

from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._kit import warning

DESCRIPTION = "A coin-slot piggy bank carries a warning triangle at its flank."


def draw(s):
    tail = []
    for angle in range(5, 426, 10):
        radius = 9.5 - .017 * (angle - 5)
        a = radians(angle)
        tail.append((2 + radius * cos(a), 12, 25 + radius * sin(a)))
    s.tube(tail, 1.05)
    for x, y in ((15, -11), (41, -11), (15, 11), (42, 11)):
        s.box(x, y, 0, 10, 9, 13, 2.8)

    sections = ((8, 14, 9), (12, 23, 15), (24, 29, 20), (34, 26, 17),
                (42, 19, 12), (46, 8, 5), (47, 1, 1))
    body = MultiPoint([project((x, y, z))
                       for z, rx, ry in sections
                       for x, y in oval(29, 0, rx, ry, count=40)]).convex_hull
    s.layers.append((body.boundary, body, EDGE))
    s.ellipse(27, -1, 46.4, 9, 1.6, EDGE)

    s.face([(40, -10, 38), (37, -10, 47), (37, -10, 52), (40, -10, 54),
            (46, -10, 48), (51, -10, 42), (50, -10, 37)])
    s.face([(38, 10, 39), (35, 10, 46), (36, 10, 52), (39, 10, 54),
            (46, 11, 49), (49, 12, 43), (46, 12, 37)])

    tip = [(65, y, z) for y, z in oval(0, 22, 8.6, 6.8, count=38)]
    base = [(53, y, z) for y, z in oval(0, 23, 10.5, 8, count=38)]
    snout = MultiPoint([project(point) for point in tip + base]).convex_hull
    s.layers.append((snout.boundary, snout, EDGE))
    s.face(tip)
    for y in (-3.4, 3.4):
        s.line([(65.1, y, 20.5), (65.1, y, 23.8)], DETAIL)
    s.line([(51, y, z) for y, z in oval(13, 31, 1.55, 1.55, count=16)], EDGE)
    warning(s, 28, 24, 29, 21)
