from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_line, desk_sheet, magnifier, rule

DESCRIPTION = "A magnifier centers on a bracketed citation marker beside a reference entry."


def draw(s):
    point = desk_sheet(s, 104, 71)
    rule(s, point, 13, 54, 55, EDGE)
    for x, direction in ((24, -1), (40, 1)):
        chart_line(s, point, [(x, 38), (x + 4*direction, 38),
                              (x + 4*direction, 24), (x, 24)], EDGE)
    rule(s, point, 27, 31, 10, EDGE)
    rule(s, point, 58, 36, 33, EDGE)
    rule(s, point, 58, 26, 24, DETAIL)
    x, y, z = point(32, 31)
    magnifier(s, x, y + 1, z, 24, direction=(-.64, -.77))
