from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import board, chart_line, response_curve

DESCRIPTION = "An adoption chart stays flat before rising, with a clock badge marking the delayed start."


def draw(s):
    p = board(s, 131, 83, run=.30, rise=.78, depth=8, level=True)
    s.line([p(14, 74), p(14, 12), p(122, 12)], EDGE)
    for x in (24, 61):
        s.line([p(x, 14), p(x, 44)], DETAIL, dashed=True)
    chart_line(s, p, [(x + 15, 21 + z*.76) for x, z in response_curve()])
    badge(s, "clock", *p(43, 12), 12)
