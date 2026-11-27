from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "A standing chart samples a wavy signal with evenly spaced stems."


def draw(s):
    f = chart_board(s)
    curve = [(14 + t, 38 + 16*sin(t/11) + 6*sin(t/4.5)) for t in range(0, 89, 2)]
    s.line([f(u, v) for u, v in curve], EDGE)
    for t in range(4, 89, 12):
        v = 38 + 16*sin(t/11) + 6*sin(t/4.5)
        s.line([f(14 + t, 10), f(14 + t, v)], DETAIL)
        dot(s, f, 14 + t, v, 2.4, BOLD)
