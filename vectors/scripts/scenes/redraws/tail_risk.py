from math import exp

from scenes.redraws._kit import warning
from scenes.redraws._w2 import axes, board, chart_line

DESCRIPTION = "A loss distribution trails off into a long right tail marked by a warning triangle."


def draw(s):
    point = board(s, 123, 79, run=.44, rise=.79, level=True)
    axes(s, point, width=100, height=58)
    curve = [(x, 16 + 51 * ((x - 12) / 15) ** 2 * exp(2 - 2 * (x - 12) / 15))
             for x in range(13, 109)]
    chart_line(s, point, curve)
    warning(s, 50, -60, 26, 26)
