from geometry import DETAIL, EDGE, GUIDE
from scenes.redraws._kit import glyph

DESCRIPTION = "A home battery hangs on a garage wall above a marked floor clearance."


def draw(s):
    s.box(-40, -9, 0, 80, 53, 4, 1)
    s.box(-40, -9, 4, 80, 7, 68, 1)
    s.box(-40, -2, 4, 5, 20, 68, 1)
    s.line([(-35, -2, 11), (40, -2, 11)], DETAIL)
    s.box(-21, -2, 19, 35, 5, 6, 1, DETAIL)
    s.box(-25, -2, 21, 43, 10, 43, 4)
    glyph(s, "bolt", -3, 8, 43, 11, EDGE)
    s.line([(-4, 8, 28), (2, 8, 28)], DETAIL)
    s.line([(21, 8, 21), (31, 8, 21)], GUIDE, dashed=True)
    s.line([(27, 8, 4), (27, 8, 21)], EDGE)
    for z in (4, 21):
        s.line([(24, 8, z - 1.5), (30, 8, z + 1.5)], DETAIL)
