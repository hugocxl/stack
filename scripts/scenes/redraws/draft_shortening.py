from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_line, draft_notebook, rule

DESCRIPTION = "A minus badge sits beside a short retained paragraph beneath four faded lines in a notebook."


def draw(s):
    point = draft_notebook(s)
    for z, width in ((70, 58), (61, 53), (52, 60), (43, 47)):
        chart_line(s, point, [(12, z), (12 + width, z)], DETAIL, dash=(5, 4))
    for z, width in ((27, 51), (17, 37)):
        rule(s, point, 12, z, width, EDGE)
    badge(s, "minus", *point(83, 36), 13)
