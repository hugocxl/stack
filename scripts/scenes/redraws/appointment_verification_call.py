from math import cos, radians, sin

from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface, bezier_path

DESCRIPTION = "A thick telephone handset carries a check badge beside one earpiece."


def draw(s):
    angle = radians(26)
    c, q = cos(angle), sin(angle)
    handset = Surface(s, lambda u, v: (c*u - q*v, -.28*(q*u + c*v), 27 + q*u + c*v))
    outline = bezier_path(
        (-42, 0),
        ((-46, 6), (-44, 15), (-37, 22)),
        ((-18, 39), (18, 39), (37, 22)),
        ((44, 15), (46, 6), (42, 0)),
        ((39, -5), (28, -9), (23, -4)),
        ((19, 0), (17, 8), (18, 12)),
        ((19, 15), (22, 16), (24, 18)),
        ((12, 26), (-12, 26), (-24, 18)),
        ((-22, 16), (-19, 15), (-18, 12)),
        ((-17, 8), (-19, 0), (-23, -4)),
        ((-28, -9), (-39, -5), (-42, 0)),
    )
    handset.slab(outline[:-1], 9)
    for x in (-33, 33):
        handset.frame(x - 5, 1, 10, 5, 2.4, DETAIL)
    badge(s, "check", *handset.at(45, 14), 13)
