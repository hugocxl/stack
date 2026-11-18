from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, desk_sheet, rule, sparkle

DESCRIPTION = "A folded writing page shows a dark cursor followed by dashed ghost text beneath a four-point sparkle."


def draw(s):
    point = desk_sheet(s, 108, 83, fold=14, depth=5)
    rule(s, point, 13, 62, 47, EDGE)
    rule(s, point, 13, 46, 73)
    rule(s, point, 13, 29, 32, EDGE)
    chart_line(s, point, [(51, 19), (51, 39)], BOLD)
    for start, length in ((59, 8), (72, 7), (84, 10)):
        rule(s, point, start, 29, length, DETAIL)
    sparkle(s, point, 79, 58, 10, EDGE)
