from math import cos, radians, sin

from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project, rounded

DESCRIPTION = "A multi-loop stretching strap rests on a partially unrolled exercise mat."


def draw(s):
    left, right, center, radius = -40, 40, -26, 10
    s.solid(rounded(left, center, right - left, 79, 5), 0, 2, crease=False)

    rim = oval(center, radius, radius, radius, count=64)
    ends = [[(x, y, z) for y, z in rim] for x in (left, right)]
    roll = MultiPoint([project(p) for end in ends for p in end]).convex_hull
    s.layers.append((roll.boundary, roll, EDGE))
    s.line(ends[-1], EDGE)

    spiral = []
    for step in range(91):
        a = radians(-92 + 8*step)
        r = 8.3 - 7.1*step/90
        spiral.append((right, center + r*cos(a), radius + r*sin(a)))
    s.line(spiral, DETAIL)

    def place(u, v):
        return (u + .35*v + 4, .23*u + v + 25, 3)

    strap = [(-36, -9), (-31, -13), (-14, -13), (-10, -9), (27, -8),
             (32, -4), (32, 4), (27, 8), (-10, 8), (-15, 13),
             (-32, 13), (-36, 8)]
    loops = [rounded(-32, -9, 17, 18, 5), rounded(-10, -5, 11, 10, 3),
             rounded(4, -5, 11, 10, 3), rounded(18, -5, 11, 10, 3)]
    s.face([place(u, v) for u, v in strap],
           openings=[[place(u, v) for u, v in loop] for loop in loops])
