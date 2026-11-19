from geometry import EDGE
from scenes.redraws._w2 import chart_marker, rule, standing_notebook

DESCRIPTION = "A spiral drafting notebook shows bullets and text rules at three indentation levels."


def draw(s):
    point = standing_notebook(s, 85, 110)
    rule(s, point, 13, 86, 38, EDGE)
    rows = ((68, 0, 38), (54, 1, 32), (40, 2, 22), (26, 2, 30), (12, 0, 29))
    for z, depth, width in rows:
        x = 15 + depth*9
        chart_marker(s, point, x, z, 2.15, EDGE)
        rule(s, point, x + 7, z, width, EDGE)
