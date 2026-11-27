from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "A standing chart shows demand bars with the next bars outlined in dashes as a forecast."


def draw(s):
    f = chart_board(s)
    for i, h in enumerate((18, 26, 22, 34, 40, 48)):
        u = 20 + i*14
        pts = [(u, 10), (u, 10 + h), (u + 8, 10 + h), (u + 8, 10)]
        s.line([f(*p) for p in pts], EDGE if i < 4 else DETAIL, dashed=i >= 4)
