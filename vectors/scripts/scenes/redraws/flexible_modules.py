from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "Two matching rounded modules sit side by side, joined by a short connector peg."


def draw(s):
    s.box(-62, -24, 0, 48, 48, 40, 6)
    s.tube([(-14, 0, 20), (14, 0, 20)], 5, EDGE)
    s.box(14, -24, 0, 48, 48, 40, 6)
    for x in (-62, 14):
        s.line([(x + 10, 24, 30), (x + 38, 24, 30)], DETAIL)
