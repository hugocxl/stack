from math import cos, exp, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import chart_board, dot, smooth

DESCRIPTION = "A standing chart splits a signal into three stacked traces: original, trend and season."


def draw(s):
    f = chart_board(s, axes=False)
    for base, amp, slope, ink in ((56, 6, .12, BOLD), (36, 0, .18, EDGE), (18, 6, 0, DETAIL)):
        s.line([f(10 + t, base + slope*(t - 46) + amp*sin(t/6)) for t in range(0, 93, 2)], ink)
