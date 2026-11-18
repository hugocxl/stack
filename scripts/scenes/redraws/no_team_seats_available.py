from geometry import EDGE
from scenes.redraws._kit import glyph, warning

DESCRIPTION = "Three seats on a shared bench have checked backrests and a warning triangle beside them."


def seat(s, x):
    s.box(x, 1, 11, 29, 7, 37, 4)
    s.box(x, 6, 12, 29, 27, 7, 4)
    glyph(s, "check", x + 14.5, 8, 35, 8, EDGE)


def draw(s):
    s.box(1, 12, 0, 7, 15, 12, 2)
    s.box(94, 12, 0, 7, 15, 12, 2)
    s.box(0, 15, 8, 103, 10, 5, 2)
    for x in (0, 37, 74):
        seat(s, x)
    warning(s, 111, 5, 44, 34)
