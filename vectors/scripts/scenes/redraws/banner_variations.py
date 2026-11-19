from math import cos, radians, sin

from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_marker, rule, upright_face

DESCRIPTION = "Three fanned campaign banners move the same round motif between left, right, and center layouts."


def draw(s):
    layouts = (
        (0, -12, 45, 12, 21, 20, (40,)),
        (3, -6, 27, 3, 82, 16, (11,)),
        (6, 0, 10, -8, 51, 16, (13, 68)),
    )
    for x, y, z, angle, motif_x, motif_z, positions in layouts:
        ca, sa = cos(radians(angle)), sin(radians(angle))

        def point(u, v):
            return (x + .68*u*ca - v*sa, y - .32*u*ca, z + u*sa + v*ca)

        upright_face(s, point, rounded(0, 0, 104, 32, 3), 3)
        chart_marker(s, point, motif_x, motif_z, 9, EDGE)
        for start in positions:
            rule(s, point, start, 19, 23, EDGE)
            rule(s, point, start, 12, 17, DETAIL)
