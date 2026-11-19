from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A software carton marked with code brackets carries a check badge at its front-right corner."


def draw(s):
    s.box(0, 0, 0, 60, 33, 42, 2)
    s.line([(2, 33, 34), (59, 33, 34), (60, 2, 34)], DETAIL)
    s.line([(28, 2, 42), (28, 31, 42)], EDGE)
    for points in ([(23, 25), (15, 18), (23, 11)], [(35, 26), (28, 10)],
                   [(41, 25), (49, 18), (41, 11)]):
        s.line([(x, 33, z) for x, z in points], BOLD)
    badge(s, "check", 62, 8, 36, 12.8)
