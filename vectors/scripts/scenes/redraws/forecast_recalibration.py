from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_line, chart_marker, laptop

DESCRIPTION = "A refresh badge sits at the point where a dashed forecast bends away from its former course."


def draw(s):
    p = laptop(s, 127, 75)
    s.line([p(13, 69), p(13, 17), p(113, 17)], EDGE)
    pivot = (61, 43)
    chart_line(s, p, [(17, 27), (29, 33), (41, 29), (50, 40), pivot], BOLD)
    chart_line(s, p, [pivot, (85, 38), (113, 32)], DETAIL, dash=(3, 3.5))
    chart_line(s, p, [pivot, (80, 54), (100, 57), (113, 66)], EDGE, dash=(4.7, 3.3))
    chart_marker(s, p, *pivot, 3, BOLD)
    s.line([p(61, 17), p(61, 39)], DETAIL, dashed=True)
    badge(s, "refresh", 59, 3, 60, 10)
