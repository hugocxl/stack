from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import axes, chart_line, chart_marker, desktop_monitor

DESCRIPTION = "A monitor compares two falling cohort lines across the same elapsed-time axis."


def draw(s):
    p = desktop_monitor(s, 128, 90)
    axes(s, p, x=14, y=35, width=99, height=60)
    for z in (49, 64, 79):
        s.line([p(10, z), p(14, z)], DETAIL)
    first = [(19, 91), (36, 80), (55, 71), (76, 68), (101, 65), (112, 64)]
    second = [(19, 82), (36, 66), (55, 55), (76, 49), (101, 44), (112, 43)]
    chart_line(s, p, first, BOLD)
    chart_line(s, p, second, EDGE)
    for x, z in first[::2]:
        chart_marker(s, p, x, z, 3, EDGE)
    for x, z in second[::2]:
        s.face([p(x, z + 3.8), p(x + 3.8, z), p(x, z - 3.8), p(x - 3.8, z)], EDGE)
