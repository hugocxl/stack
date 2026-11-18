from math import cos, radians, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._w2 import chart_line, closed_outline, folded_sheet, rule

DESCRIPTION = "An estimate pad shows a fan behind a square grille above three aligned item and price rows."


def draw(s):
    def point(x, z):
        return .48*x, -.52*x - .38*z, .91*z

    folded_sheet(s, point, 72, 86, fold=11, depth=9)
    closed_outline(s, point, [(13, 42), (49, 42), (49, 78), (13, 78)], EDGE)
    closed_outline(s, point, oval(31, 60, 14.5, 14.5), EDGE)
    for angle in (0, 120, 240):
        c, a = cos(radians(angle)), sin(radians(angle))
        vane = [(2, 1), (4, 8), (8, 8), (11, 4), (8, 0), (2, -1)]
        chart_line(s, point, [(31 + x*c - y*a, 60 + x*a + y*c) for x, y in vane], EDGE)
    closed_outline(s, point, oval(31, 60, 2, 2), DETAIL)
    for z, length in ((34, 28), (25, 34), (16, 24)):
        rule(s, point, 13, z, length)
        rule(s, point, 53, z, 8, EDGE)
    chart_line(s, point, [(48, 12), (63, 12)], DETAIL)
    rule(s, point, 52, 6, 10, EDGE)
