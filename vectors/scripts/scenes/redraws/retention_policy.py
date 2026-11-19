from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "A ring-bound records policy book shows a bracketed date range beside a clock badge."


def draw(s):
    face = lambda x, z: (x, -z * .54, z)
    panel(s, rounded(0, 0, 68, 58, 3), face, 9)
    for x in (14, 54):
        s.tube([(x, -36, 55), (x, -37, 61), (x, -34, 64),
                (x, -29, 63), (x, -27, 59), (x, -28, 52)], 1.25)
    s.line([face(8, 44), face(46, 44)], EDGE)
    for x in (15, 49):
        rect(s, face, x - 4.6, 28, 9.2, 11, .8, EDGE)
        s.line([face(x - 4.6, 35), face(x + 4.6, 35)], DETAIL)
    s.line([face(24, 33), face(40, 33)], DETAIL)
    s.line([face(9, 23), face(9, 19), face(56, 19), face(56, 23)], EDGE)
    s.line([face(9, 9), face(37, 9)], DETAIL)
    badge(s, "clock", *face(69, 14), 13)
