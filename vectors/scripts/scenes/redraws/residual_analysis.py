from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_marker, plot_point

DESCRIPTION = "A residual plot has individual stems extending above and below its zero baseline."


def draw(s):
    p = plot_point
    s.line([p(0, 7), p(0, 82)], EDGE)
    s.line([p(0, 42), p(113, 42)], BOLD)
    for z in (14, 28, 56, 70):
        s.line([p(-5, z), p(0, z)], DETAIL)
    for x, z in ((14, 56), (28, 33), (42, 64), (56, 49), (70, 20), (84, 29), (98, 54)):
        s.line([p(x, 42), p(x, z)], EDGE)
        chart_marker(s, p, x, z, 2.5, EDGE)
