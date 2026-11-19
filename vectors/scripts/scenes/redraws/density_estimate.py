from math import exp

from geometry import BOLD, EDGE
from scenes.redraws._w2 import chart_line, ground_plot

DESCRIPTION = "A smooth density curve rises above a row of sample ticks clustered along its baseline."


def draw(s):
    p = ground_plot(s, 120, 78)
    for x in (8, 15, 29, 33, 39, 44, 48, 53, 57, 63, 68, 72, 82, 94, 112):
        s.line([p(x, 5), p(x, 14)], EDGE)
    points = [(x, 18 + 52*exp(-((x - 48)/24)**2) + 16*exp(-((x - 83)/21)**2))
              for x in range(3, 119)]
    chart_line(s, p, points, BOLD)
