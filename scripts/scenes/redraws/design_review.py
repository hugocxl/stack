from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import (
    chart_line, chart_marker, closed_outline, face_magnifier, laptop, rule,
)

DESCRIPTION = "An open magnifier frames a button in the interface wireframe on a laptop screen."


def draw(s):
    point = laptop(s, width=111, height=80)
    rule(s, point, 6, 67, 99, DETAIL)
    for x in (12, 18, 24):
        chart_marker(s, point, x, 72, 1.25, EDGE)
    closed_outline(s, point, rounded(13, 24, 36, 33, 2), DETAIL)
    chart_line(s, point, [(16, 28), (26, 42), (32, 35), (38, 40), (46, 28)], DETAIL)
    chart_marker(s, point, 39, 48, 3, DETAIL)
    rule(s, point, 60, 54, 33, EDGE)
    rule(s, point, 60, 46, 28, DETAIL)
    closed_outline(s, point, rounded(62, 27, 28, 12, 4), EDGE)
    rule(s, point, 70, 33, 12, DETAIL)
    face_magnifier(s, point, 76, 33, 20)
