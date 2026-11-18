from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, rule, standing_notebook

DESCRIPTION = "A ring-bound policy manual has a boxed approval section marked with a large check badge."


def draw(s):
    point = standing_notebook(s, 96, 91)
    rule(s, point, 13, 65, 51, EDGE)
    rule(s, point, 13, 54, 68)
    rule(s, point, 13, 46, 49)
    closed_outline(s, point, rounded(12, 11, 72, 26, 3), EDGE)
    rule(s, point, 20, 27, 30, EDGE)
    rule(s, point, 20, 20, 25, DETAIL)
    badge(s, "check", *point(80, 25), 16)
