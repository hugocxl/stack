from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, ground_plot, response_curve

DESCRIPTION = "A cumulative probability curve rises from zero and flattens at the top of a ruled probability scale."


def draw(s):
    p = ground_plot(s, 113, 77)
    for z in (22, 40, 58, 76):
        s.line([p(-4, z), p(0, z)], EDGE)
    chart_line(s, p, [(2, 76), (110, 76)], DETAIL, dash=(4, 4))
    chart_line(s, p, [(x + 1, 5 + z*71/62) for x, z in response_curve()], BOLD)
