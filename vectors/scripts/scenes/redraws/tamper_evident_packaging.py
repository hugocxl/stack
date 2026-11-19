from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import glyph

DESCRIPTION = "An intact lock-marked security strip bridges the lid seam and folds over the front of a shipping carton."


def draw(s):
    x, y, z = 35, 27, 45
    s.face([(-x, -y, z), (x, -y, z), (x, y, z), (-x, y, z)], EDGE)
    s.face([(x, -y, 0), (x, y, 0), (x, y, z), (x, -y, z)], EDGE)
    s.face([(-x, y, 0), (x, y, 0), (x, y, z), (-x, y, z)], EDGE)

    # A single seal spans the flap joint and turns down over the same fold.
    s.line([(-x, 2, z), (-13, 2, z)], DETAIL)
    s.line([(13, 2, z), (x, 2, z)], DETAIL)
    s.line([(-13, y, z), (-13, -12, z), (13, -12, z), (13, y, z)], BOLD)
    s.line([(-13, y, z), (-13, y, 15), (13, y, 15), (13, y, z)], BOLD)
    for mark in (-9, 9):
        s.line([(mark, -9, z), (mark, y - 3, z)], DETAIL, dashed=True)
    glyph(s, "lock", 0, y, 29, 12, EDGE)
