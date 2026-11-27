from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "A standing chart keeps its trend under a dashed guardrail line marked by a shield badge."


def draw(s):
    f = chart_board(s)
    s.line([f(12, 54), f(102, 54)], EDGE, dashed=True)
    s.line([f(u, v) for u, v in [(14, 22), (28, 30), (42, 26), (56, 38), (70, 34), (84, 42), (100, 40)]], BOLD)
    badge(s, "lock", *f(100, 62), 10)
