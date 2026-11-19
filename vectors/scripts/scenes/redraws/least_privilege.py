from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w5 import panel, physical_key, rect

DESCRIPTION = "A key sits in the single enabled slot of a three-cell permissions block."


def draw(s):
    face = lambda x, z: (x, -.23 * z, z)
    panel(s, rounded(0, 0, 73, 35, 4), face, 12)
    for center in (15, 36.5, 58):
        rect(s, face, center - 8, 8, 16, 18, 2,
             EDGE if center == 36.5 else DETAIL)
        if center != 36.5:
            s.line([face(center - 3, 17), face(center + 3, 17)], DETAIL)
    s.line([face(35, 13), face(35, 21), face(38, 21), face(38, 13)], EDGE)
    key = lambda x, z: (15.5 + .87 * x + .3 * z,
                        12 - .66 * x, 43 - 1.04 * x + .95 * z)
    physical_key(s, key)
