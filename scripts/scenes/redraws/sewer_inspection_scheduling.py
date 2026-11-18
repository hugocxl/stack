from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A round cast-iron manhole cover carries a clock badge at its rim."


def draw(s):
    s.disk(0, 0, 0, 33, 33, 9)
    s.ellipse(0, 0, 9, 28.5, 28.5, EDGE)
    s.ellipse(0, 0, 9, 25, 25, DETAIL)
    for y in (-12, -4, 4, 12):
        for x in (-10, 0, 10):
            s.line([(x - 3, y, 9), (x + 3, y, 9)], EDGE)
    for x in (-18, 18):
        s.ellipse(x, 0, 9, 1.7, 3, EDGE)
    badge(s, "clock", 18, -20, 10, 13)
