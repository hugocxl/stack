from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import (
    chart_line, chart_marker, closed_outline, rule, standing_notebook,
)

DESCRIPTION = "A spiral storyboard shows three sequential sketch panels and a plus badge."


def draw(s):
    point = standing_notebook(s, 113, 72)
    for x in (8, 42, 76):
        closed_outline(s, point, rounded(x, 27, 29, 26, 1), EDGE)
        rule(s, point, x, 19, 24)
        rule(s, point, x, 12, 15)
    chart_marker(s, point, 25, 43, 4, EDGE)
    chart_line(s, point, [(10, 31), (18, 36), (26, 31), (35, 35)], EDGE)
    chart_line(s, point, [(44, 32), (50, 32), (56, 46), (63, 33), (69, 37)], EDGE)
    chart_line(s, point, [(79, 33), (79, 43), (91, 49), (102, 42), (102, 33)], EDGE)
    closed_outline(s, point, [(88, 33), (88, 41), (94, 41), (94, 33)], EDGE)
    badge(s, "plus", *point(112, 65), 11)
