from geometry import BOLD, EDGE
from scenes.redraws._w2 import chart_line, chart_marker, ground_plot

DESCRIPTION = "Two opposing response lines cross on a shared ruled axis."


def draw(s):
    p = ground_plot(s, 112, 75)
    series = ((BOLD, [(12, 22), (40, 29), (69, 49), (100, 74)]),
              (EDGE, [(12, 68), (40, 53), (69, 38), (100, 30)]))
    for ink, points in series:
        chart_line(s, p, points, ink)
        for x, z in (points[0], points[-1]):
            chart_marker(s, p, x, z, 3.5, ink)
