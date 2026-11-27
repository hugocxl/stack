from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "A standing chart carries a solid renewal history that continues as a dashed forecast."


def draw(s):
    f = chart_board(s)
    s.line([f(u, v) for u, v in [(14, 18), (28, 26), (40, 24), (54, 36)]], BOLD)
    s.line([f(u, v) for u, v in [(54, 36), (70, 44), (84, 50), (100, 60)]], EDGE, dashed=True)
    dot(s, f, 54, 36, 3.2, BOLD)
