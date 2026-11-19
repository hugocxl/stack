from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A clock badge attaches to a timber workbench with a built-in screw vise."


def draw(s):
    for x, y in ((7, 6), (78, 6), (7, 46), (78, 46)):
        s.box(x, y, 0, 8, 8, 49, 1)
    s.box(10, 48, 16, 72, 4, 7, 1)
    s.box(6, 11, 16, 5, 43, 7, 1)
    s.box(4, 47, 37, 83, 6, 11, 1)
    s.box(0, 0, 47, 94, 59, 8, 3)
    s.box(13, 44, 55, 25, 11, 8, 2)
    s.tube([(25, 52, 49), (25, 70, 49)], 2.9, EDGE)
    s.box(13, 65, 46, 25, 7, 17, 2)
    s.tube([(25, 73, 52), (25, 79, 52)], 3.25, EDGE)
    s.tube([(15, 79, 58), (34, 79, 46)], 1.6, DETAIL)
    badge(s, "clock", 98, 15, 62, 15)
