from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow

DESCRIPTION = "A service loading door is raised above a threshold with an inward arrow."


def draw(s):
    s.box(0, 0, 0, 64, 38, 4, 1.5)
    s.box(0, 0, 4, 64, 6, 58, 1)
    s.box(0, 4, 4, 7, 14, 57, 1)
    s.box(57, 4, 4, 7, 14, 57, 1)
    s.box(0, 7, 49, 64, 11, 13, 1.5)
    s.box(7, 13, 34, 50, 3, 15, .7)
    for z in (39, 44):
        s.line([(8, 16, z), (56, 16, z)], DETAIL)
    s.line([(9, 18, 4.1), (55, 18, 4.1)], EDGE)
    arrow(s, [(32, 35, 4.2), (32, 15, 4.2)], BOLD, head=8)
