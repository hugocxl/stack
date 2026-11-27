from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "A standing chart traces an S-shaped curve that rises from zero and levels off at the top."


def draw(s):
    f = chart_board(s)
    s.line([f(12, 62), f(102, 62)], DETAIL, dashed=True)
    curve = [(14 + t, 12 + 50/(1 + exp(-(t - 44)/8))) for t in range(0, 89, 3)]
    s.line([f(u, v) for u, v in curve], BOLD)
