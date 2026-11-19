from math import cos, radians, sin

from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, upright_face

DESCRIPTION = "A strip of film shows two outlined paper-plane poses around a dashed intermediate pose."


def draw(s):
    def point(x, z):
        return .76*x, -.24*x - .21*z, z

    upright_face(s, point, rounded(0, 0, 140, 66, 4), 5)
    for x in range(9, 136, 14):
        for z in (5, 56):
            closed_outline(s, point, rounded(x - 3.8, z, 7.6, 5, 1), DETAIL)
    for x, angle in ((24, 27), (70, 0), (116, -27)):
        closed_outline(s, point, rounded(x - 19, 15, 38, 36, 1), EDGE)
        c, s_ = cos(radians(angle)), sin(radians(angle))

        def pose(u, v):
            return point(x + u*c - v*s_, 33 + u*s_ + v*c)

        outline = [(-13, 8), (16, 0), (-12, -8), (-7, 0), (-13, 8)]
        if angle:
            chart_line(s, pose, outline, BOLD)
            chart_line(s, pose, [(-7, 0), (10, 0)], DETAIL)
        else:
            chart_line(s, pose, outline, EDGE, dash=(3, 2))
