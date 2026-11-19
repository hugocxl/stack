from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "A segmented quota meter stops just short of a heavy capacity line."


def draw(s):
    face = lambda x, z: (x, -.27 * z, z)
    panel(s, rounded(0, 0, 84, 39, 5), face, 14)
    rect(s, face, 8, 11, 58, 15, 2, DETAIL)
    for x in (12, 21, 30, 39, 48):
        rect(s, face, x, 14, 6, 9, .9, EDGE)
    s.line([face(63, 7), face(63, 30)], BOLD)
    for x in (12, 30, 48):
        s.line([face(x, 7), face(x, 9)], DETAIL)
