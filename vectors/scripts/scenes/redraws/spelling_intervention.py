from math import pi, sin

from geometry import BOLD, EDGE, rounded
from scenes.editorial_objects import At, pencil
from scenes.redraws._w2 import chart_line, upright_face

DESCRIPTION = "A pencil rests beside a proofreading card with a wavy underline beneath a short run of type."


def draw(s):
    def point(x, z):
        return x, -.23*z, z

    upright_face(s, point, rounded(0, 0, 85, 56, 4), 6)
    typeset = (
        [(13, 27), (13, 35), (19, 35), (21, 32), (21, 27)],
        [(25, 28), (26, 33), (31, 34), (34, 31), (32, 27), (27, 27)],
        [(39, 40), (39, 30), (41, 27), (45, 27)],
        [(49, 29), (50, 34), (55, 34), (57, 31), (54, 27), (50, 27)],
        [(62, 27), (62, 36), (67, 36), (69, 32), (69, 27)],
    )
    for stroke in typeset:
        chart_line(s, point, stroke, EDGE)
    chart_line(s, point, [(12 + i*1.45, 18 + 2.15*sin(i*pi/4))
                          for i in range(40)], BOLD)
    pencil(At(s, 53, -6, 0, .77))
