from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import glyph

DESCRIPTION = "A freestanding pool sign shows a ladder above two clock faces joined by a short line."


def draw(s):
    for x in (10, 57):
        s.box(x, -4, 0, 7, 10, 3, 1.2)
        s.box(x + 1, -2, 3, 5, 5, 37, 1.2)
    s.box(0, -4, 21, 74, 7, 44, 3)
    y = 3
    for x in (29, 37):
        s.line([(x, y, 49), (x, y, 57), (x + 2, y, 59), (x + 5, y, 59)], BOLD)
    s.line([(29, y, 54), (37, y, 54)], EDGE)
    for z in (46, 50):
        s.line([(x, y, z + dz) for x, dz in
                ((20, 0), (24, 1.7), (28, 0), (32, -1.7), (36, 0), (40, 1.7), (44, 0), (48, -1.7), (52, 0))], EDGE)
    for x in (24, 50):
        s.line([(a, y, b) for a, b in oval(x, 33, 6.4, 6.4, count=35)], EDGE)
    glyph(s, "clock", 24, y, 33, 5.6, DETAIL)
    s.line([(50, y, 29), (50, y, 33), (46, y, 33)], DETAIL)
    s.line([(34, y, 33), (40, y, 33)], EDGE)
