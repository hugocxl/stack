from geometry import DETAIL, EDGE, GUIDE
from scenes.redraws._kit import arrow, badge

DESCRIPTION = "An empty office chair pulled away from its desk carries a clock badge for a movement break."


def draw(s):
    for x in (5, 75):
        s.box(x, 4, 0, 6, 8, 56, 1)
        s.box(x, 35, 0, 6, 8, 56, 1)
    s.box(0, 0, 56, 87, 48, 5, 3)
    s.box(23, 6, 61, 39, 5, 28, 2)
    s.line([(25, 11, 64), (60, 11, 64)], DETAIL)

    s.line([(67, 47, 0), (67, 74, 0)], GUIDE, dashed=True)
    arrow(s, [(67, 77, 0), (67, 95, 0)], EDGE, head=6)

    # The chair faces the desk, with its back turned toward the viewer.
    for x, y in ((23, 70), (34, 57), (50, 68), (46, 84), (29, 85)):
        s.tube([(37, 72, 8), (x, y, 4)], 1.7, EDGE)
        s.disk(x, y, 0, 2.9, 2.9, 4, DETAIL)
    s.disk(37, 72, 7, 3, 3, 22)
    s.box(19, 58, 29, 36, 31, 6, 5)
    s.tube([(37, 81, 34), (37, 89, 40), (37, 89, 49)], 2.1, EDGE)
    s.box(19, 86, 45, 36, 7, 24, 3)
    s.line([(24, 93, 63), (49, 93, 63)], DETAIL)
    badge(s, "clock", 58, 88, 72, 15)
