from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "On a standing chart two response lines cross between their end markers."


def draw(s):
    f = chart_board(s)
    for a, b in (((18, 20), (96, 58)), ((18, 58), (96, 22))):
        s.line([f(*a), f(*b)], BOLD)
        dot(s, f, *a, 3)
        dot(s, f, *b, 3)
