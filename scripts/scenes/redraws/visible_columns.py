from math import sin, pi

from geometry import EDGE
from scenes.redraws._w4 import standing_card

DESCRIPTION = "A table of three columns has an eye symbol set into the header of the selected column."


def draw(s):
    face = standing_card(s, 109, 77, angle=-26, lean=.35, depth=7)
    face.frame(9, 10, 91, 57, 2, EDGE)
    for u in (39, 70):
        face.line([(u, 10), (u, 67)], EDGE)
    for v in (22, 34):
        face.line([(9, v), (100, v)])
    face.line([(9, 46), (100, 46)], EDGE)
    face.frame(42, 13, 25, 51, 2, EDGE)
    for u in (23, 85):
        face.rows(u - 6, 57, (12,))
    for sign in (-1, 1):
        face.line([(44 + 21*i/16, 56 + sign*5*sin(pi*i/16))
                   for i in range(17)], EDGE)
    face.oval(54.5, 56, 2.8, 3.4, EDGE)
    for v in (40, 16):
        for u, width in ((18, 11), (48, 13), (78, 12)):
            face.rows(u, v, (width,))
