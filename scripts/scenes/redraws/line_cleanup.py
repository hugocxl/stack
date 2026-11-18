from math import pi, sin

from shapely.geometry import MultiPoint

from geometry import BOLD, DETAIL, EDGE, oval, project, rounded
from scenes.redraws._w2 import chart_line, closed_outline, upright_face

DESCRIPTION = "An eraser touches the end of a smooth inked leaf contour on a bound sketchbook page."


def draw(s):
    def point(x, z):
        return .57*x, -.43*x - .56*z, .77*z

    upright_face(s, point, rounded(-20, -4, 122, 91, 5), 8)
    closed_outline(s, point, rounded(-12, 2, 108, 79, 3), DETAIL)
    for z in (19, 42, 65):
        a, b, c = point(-13, z)
        s.tube([(x, y, c) for x, y in oval(a - 1, b + 2, 5, 3, 15, 308, 24)],
               1.2, EDGE)
    steps = [i / 20 for i in range(21)]

    def edge(t, side):
        bend = side * 13 * sin(pi * t)
        return 34 + 40*t - .66*bend, 33 + 38*t + .75*bend

    chart_line(s, point, [edge(t, 1) for t in steps] + [edge(t, -1) for t in reversed(steps)],
               BOLD)
    chart_line(s, point, [(23, 24), (30, 29), (34, 33), (47, 48), (61, 61)], EDGE)

    def top(x, z):
        a, b, c = point(x, z)
        return a + 2, b + 5, c + 10

    footprint = rounded(7, 12, 19, 14, 2.5)
    lower, upper = ([surface(x, z) for x, z in footprint] for surface in (point, top))
    hull = MultiPoint([project(p) for p in lower + upper]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.face(upper, EDGE)
    s.line([top(17, 26), top(17, 12), point(17, 12)], DETAIL)
