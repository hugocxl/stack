from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_line, closed_outline, folded_sheet, rule

DESCRIPTION = "A folded data file shows a grid of repeatable test records and a plus badge at its corner."


def draw(s):
    def point(x, z):
        return .74*x, -.26*x - .16*z, z

    folded_sheet(s, point, 74, 93, fold=12, depth=7)
    rule(s, point, 12, 76, 34, EDGE)
    closed_outline(s, point, rounded(11, 17, 52, 48, 2), EDGE)
    for z in (33, 49):
        rule(s, point, 11, z, 52, EDGE)
    chart_line(s, point, [(30, 17), (30, 65)], EDGE)
    for z in (25, 41, 57):
        rule(s, point, 17, z, 7, DETAIL)
        rule(s, point, 36, z, 18, DETAIL)
    badge(s, "plus", *point(74, 72), 11)
