from math import cos, radians, sin

from geometry import EDGE, rounded
from scenes.redraws._w2 import chart_marker, upright_face

DESCRIPTION = "Three planning-poker cards fan out with different counts of outlined pips."


def draw(s):
    for center, lift, tilt, pips in (
        (-32, 29, 31, ((-14, 50), (-14, 37))),
        (4, 14, 15, ((-14, 52), (0, 49), (-14, 37))),
        (34, 0, -13, ((-11, 45), (11, 45), (0, 33), (-11, 21), (11, 21))),
    ):
        angle = radians(tilt)
        c, sn = cos(angle), sin(angle)

        def point(x, z):
            u = center + x*c - z*sn
            v = lift + x*sn + z*c
            return .82*u, -.18*u - .48*v, .87*v

        upright_face(s, point, rounded(-24, 0, 48, 65, 5), 4)
        for x, z in pips:
            chart_marker(s, point, x, z, 3.35, EDGE)
