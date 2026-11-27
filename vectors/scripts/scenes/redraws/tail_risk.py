from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "A standing chart shows a loss curve trailing into a long right tail, with a warning triangle."


def draw(s):
    f = chart_board(s)
    curve = [(14 + t, 12 + 48*exp(-((t - 16)/9)**2) + 6*exp(-t/30)) for t in range(0, 89, 2)]
    s.line([f(u, v) for u, v in curve], BOLD)
    from scenes.redraws._kit import warning
    x, y, z = f(88, 22)
    warning(s, x, y + 1, z, 20)
