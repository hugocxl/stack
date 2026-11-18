from math import cos, radians, sin

from shapely.geometry import MultiPoint

from geometry import BOLD, DETAIL, EDGE, oval, project
from scenes.redraws._kit import arrow

DESCRIPTION = "A dumbbell with two thick hexagonal weights sits below a rising progression arrow."


def draw(s):
    c, q = cos(radians(20)), sin(radians(20))

    def point(u, v, z):
        return u*c + v*q, -u*q + v*c, z

    def weight(start, end):
        profile = oval(0, 16, 18, 18, count=6)[:-1]
        faces = [[point(u, v, z) for v, z in profile] for u in (start, end)]
        body = MultiPoint([project(p) for face in faces for p in face]).convex_hull
        s.layers.append((body.boundary, body, EDGE))
        s.line([*faces[1], faces[1][0]], EDGE)
        for index in (1, 2):
            s.line([faces[0][index], faces[1][index]], DETAIL)

    weight(-42, -26)
    s.tube([point(-28, 0, 16), point(28, 0, 16)], 3.6)
    weight(26, 42)

    arrow(s, [point(u, 0, z) for u, z in ((-20, 45), (-7, 52), (5, 60),
          (14, 70), (19, 81), (19, 89))], BOLD, head=9)
