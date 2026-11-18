from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, chart_marker, closed_outline, filmstrip

DESCRIPTION = "A filmstrip shows a mountain scene and a house scene separated by a dashed cut line."


def draw(s):
    p = filmstrip(s, gap=11)
    chart_line(s, p, [(11, 22), (25, 43), (37, 28), (43, 34), (51, 26)], EDGE)
    chart_marker(s, p, 42, 44, 3.4, DETAIL)
    chart_line(s, p, [(69, 23), (100, 23)], DETAIL)
    closed_outline(s, p, [(74, 23), (74, 35), (84, 44), (95, 35), (95, 23)], EDGE)
    chart_line(s, p, [(71, 33), (84, 45), (98, 33)], EDGE)
    chart_line(s, p, [(82, 23), (82, 31), (88, 31), (88, 23)], DETAIL)
    chart_line(s, p, [(59, 1), (59, 68)], BOLD, dash=(5, 4))
