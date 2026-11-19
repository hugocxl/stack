from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import standing_card

DESCRIPTION = "A standing theater seating chart shows three rows of seats split by a center aisle beneath a capacity bracket."


def draw(s):
    chart = standing_card(s, 98, 76, angle=-19, lean=.48, depth=6)
    chart.line([(10, 10), (88, 10)], DETAIL)
    chart.line([(31, 10), (36, 15), (62, 15), (67, 10)], EDGE)
    for v in (22, 36, 50):
        for u in (15, 32, 56, 73):
            chart.outline([(u, v), (u+10, v), (u+10, v+6), (u+9, v+6),
                           (u+9, v+10), (u+1, v+10), (u+1, v+6), (u, v+6)], EDGE)
            chart.line([(u+1, v+5), (u+9, v+5)], DETAIL)
    chart.line([(15, 63), (15, 68), (83, 68), (83, 63)], BOLD)
