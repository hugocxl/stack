from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "An archive carton has a tamper seal across its lid seam and a check badge at its front corner."


def draw(s):
    s.box(0, 0, 0, 57, 42, 34, 2.5)
    s.box(-1.3, -1.3, 30, 59.6, 44.6, 5, 2.5)
    for x in (22, 34):
        s.line([(x, 3, 35), (x, 43.3, 35), (x, 43.3, 30),
                (x, 42, 29), (x, 42, 19)], EDGE)
    s.line([(22, 42, 19), (26, 42, 21), (30, 42, 19), (34, 42, 21)], EDGE)
    for y in (8, 14, 20):
        s.line([(24, y, 35), (32, y + 3, 35)], DETAIL)
    badge(s, "check", 52, 43, 15, 12)
