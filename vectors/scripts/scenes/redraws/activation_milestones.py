from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "A standing chart steps up through three milestone dots to a check badge."


def draw(s):
    f = chart_board(s)
    pts = [(14, 16), (40, 16), (40, 34), (66, 34), (66, 52), (92, 52)]
    s.line([f(u, v) for u, v in pts], BOLD)
    for u, v in ((40, 16), (66, 34), (92, 52)):
        dot(s, f, u, v, 3.4)
    badge(s, "check", *f(100, 64), 11)
