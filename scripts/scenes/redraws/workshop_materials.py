from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_line, closed_outline, open_volume, rule

DESCRIPTION = "An open workshop workbook shows a ruled worksheet grid across its two pages."


def draw(s):
    left, right = open_volume(s)
    rule(s, left, 9, 55, 31, EDGE)
    rule(s, right, 9, 55, 23, EDGE)
    for leaf in (left, right):
        closed_outline(s, leaf, [(9, 11), (47, 11), (47, 45), (9, 45)], EDGE)
        for z in (22, 33):
            rule(s, leaf, 9, z, 38, DETAIL)
        chart_line(s, leaf, [(23, 11), (23, 45)], DETAIL)
