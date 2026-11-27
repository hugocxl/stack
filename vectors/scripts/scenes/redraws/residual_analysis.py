from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "A standing chart shows residual stems rising and falling from a zero line."


def draw(s):
    f = chart_board(s, axes=False)
    s.line([f(10, 38), f(102, 38)], DETAIL)
    for u, d in ((20, 14), (32, -10), (44, 20), (56, -16), (68, 8), (80, -12), (92, 16)):
        s.line([f(u, 38), f(u, 38 + d)], EDGE)
        dot(s, f, u, 38 + d, 2.4)
