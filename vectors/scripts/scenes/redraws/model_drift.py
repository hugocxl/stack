from math import exp

from geometry import BOLD, EDGE
from scenes.redraws._w2 import axes, board, chart_line

DESCRIPTION = "A solid baseline distribution and a dashed distribution with a shifted peak overlap on one monitor."


def draw(s):
    point = board(s, 120, 80, depth=11)
    axes(s, point, width=96, height=53)
    for center, spread, amplitude, style in (
        (39, 14, 49, None),
        (76, 16, 44, (5, 2.5)),
    ):
        curve = [(x, 13 + amplitude * exp(-.5 * ((x - center) / spread) ** 2))
                 for x in range(14, 108)]
        chart_line(s, point, curve, EDGE if style else BOLD, dash=style)
