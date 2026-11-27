from geometry import DETAIL, EDGE
from scenes.redraws._sf import left_face, plate

DESCRIPTION = "A service doorway has its roller shutter rolled up, with a loading arrow leading in."


def draw(s):
    wall = left_face(-60, 0, 0)
    w, h = 64, 60
    plate(s, wall, [(0, 0), (28, 0), (28, h), (28 + w, h), (28 + w, 0), (120, 0), (120, 90), (0, 90)], 6, (0, -1, 0))
    s.box(-34, -2, h, w + 4, 10, 12, 4)
    for v in (63, 67):
        s.line([(-32 + t, 8.1, v) for t in (0, w)], DETAIL)
    s.line([(-32, -6, 0), (-32 + w, -6, 0)], DETAIL)
    s.face([(-12, 40, .2), (-12, 14, .2), (-18, 14, .2), (0, 0, .2), (18, 14, .2), (12, 14, .2), (12, 40, .2)], EDGE)
