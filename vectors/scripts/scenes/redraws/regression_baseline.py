from geometry import BOLD, EDGE
from scenes.redraws._w2 import chart_line, chart_marker, ground_plot

DESCRIPTION = "One straight fitted line runs through a scatter of points above a grounded chart axis."


def draw(s):
    p = ground_plot(s, 119, 82)
    chart_line(s, p, [(6, 13), (112, 77)], BOLD)
    for x, z in ((15, 29), (25, 19), (29, 37), (41, 24), (45, 42),
                 (58, 35), (60, 53), (73, 43), (76, 64), (87, 59),
                 (99, 55), (101, 75)):
        chart_marker(s, p, x, z, 2.8, EDGE)
