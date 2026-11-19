from math import cos, radians, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import upright_profile
from scenes.systems_shapes import bezel

DESCRIPTION = "A wrench lies across the selected date on a ring-bound maintenance calendar."


def draw(s):
    for x in (-29, 29):
        s.face([(x, -18, 0), (x, 0, 0), (x, 0, 54)], DETAIL)
    s.box(-36, -4, 0, 72, 4, 56, 2)
    s.line([(-33, 0, 43), (33, 0, 43)], EDGE)
    for x in (-23, 23):
        s.tube([(x, y, z) for y, z in oval(-3, 56, 4.5, 5.5, -40, 230, 24)], 1.1, EDGE)
    for x in (-24, -8, 8, 24):
        for z in (10, 22, 34):
            bezel(s, x - 3, 0, z - 2, 6, 4, DETAIL, 1)
    bezel(s, 1, 0, 15, 14, 14, EDGE, 2)
    angle = radians(29)
    u, v = cos(angle), sin(angle)
    outline = [(-17, -2.5), (7, -2.5), (11, -6), (17, -6), (20, -3.8),
               (14, -3.8), (13, 0), (14, 3.8), (20, 3.8), (17, 6),
               (11, 6), (7, 2.5), (-17, 2.5), (-19, 0)]
    points = [(22 + a * u - b * v, 21 + a * v + b * u) for a, b in outline]
    upright_profile(s, points[::-1], 4, 2)
