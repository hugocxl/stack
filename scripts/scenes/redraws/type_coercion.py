from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import chart_marker, laptop, outline

DESCRIPTION = "A laptop screen shows a quoted token becoming a number-sign token."


def draw(s):
    point = laptop(s, 127, 67)
    for x in (14, 77):
        outline(s, x, 0, 25, 36, 29, 4)
        for u in (x + 10, x + 18, x + 26):
            chart_marker(s, point, u, 33, 1.7, EDGE)
    for x in (23, 28, 35, 40):
        s.line([point(x, 48), point(x - 1.4, 42)], BOLD)
    for x in (91, 98):
        s.line([point(x, 39), point(x + 3, 49)], BOLD)
    for z in (42, 46):
        s.line([point(89, z), point(103, z)], BOLD)
    arrow(s, [point(53, 39), point(74, 39)], EDGE, head=6)
    s.line([point(15, 62), point(41, 62)], DETAIL)
