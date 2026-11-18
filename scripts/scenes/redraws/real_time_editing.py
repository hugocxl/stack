from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, closed_outline, laptop, rule

DESCRIPTION = "Two differently flagged edit carets sit on separate lines of one shared document on a laptop."


def draw(s):
    point = laptop(s, 112, 82)
    rule(s, point, 15, 73, 33, EDGE)
    rule(s, point, 15, 61, 76, DETAIL)
    rule(s, point, 15, 46, 28, EDGE)
    rule(s, point, 53, 46, 40, DETAIL)
    rule(s, point, 15, 28, 52, EDGE)
    rule(s, point, 77, 28, 21, DETAIL)
    chart_line(s, point, [(47, 39), (47, 56)], BOLD)
    closed_outline(s, point, [(47, 55), (47, 59), (60, 59), (60, 54), (47, 54)], EDGE)
    chart_line(s, point, [(72, 21), (72, 39)], BOLD)
    closed_outline(s, point, [(72, 39), (86, 40), (81, 35), (72, 35)], EDGE)
