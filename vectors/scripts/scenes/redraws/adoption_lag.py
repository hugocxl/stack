from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "On a standing chart a flat line waits before it rises, with a clock badge at the bend."


def draw(s):
    f = chart_board(s)
    curve = smooth([(14, 16), (40, 17), (56, 20), (70, 36), (84, 56), (100, 62)], 6)
    s.line([f(u, v) for u, v in curve], BOLD)
    s.line([f(52, 12), f(52, 66)], DETAIL, dashed=True)
    badge(s, "clock", *f(52, 22), 10)
