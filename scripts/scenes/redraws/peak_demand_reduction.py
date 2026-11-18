from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow, glyph

DESCRIPTION = "A downward arrow targets the tallest column on an electricity demand chart."


def draw(s):
    s.box(-42, -18, 0, 84, 37, 13, 2.5)
    for x, height in ((-33, 10), (-20, 16), (-7, 42), (6, 19), (19, 11)):
        s.box(x, -10, 13, 8, 15, height, .9)
    s.line([(-35, 10, 13), (32, 10, 13)], DETAIL)
    glyph(s, "bolt", -30, 19, 6.5, 4.8, EDGE)
    arrow(s, [(-3, -1, 83), (-3, -1, 60)], BOLD, head=9)
