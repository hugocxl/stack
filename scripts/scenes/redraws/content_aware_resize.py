from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, chart_marker, face_arrow, landscape_frame, rule

DESCRIPTION = "Two inward arrows compress the sides of a landscape print around a centered mountain."


def draw(s):
    point = landscape_frame(s, ink=DETAIL)
    for x in (29, 81):
        chart_line(s, point, [(x, 12), (x, 74)], EDGE)
    chart_marker(s, point, 65, 58, 5, EDGE)
    chart_line(s, point, [(34, 28), (54, 54), (75, 28)], EDGE)
    rule(s, point, 34, 24, 41)
    for start, end in ((-7, 28), (117, 82)):
        face_arrow(s, point, [(start, 44), (end, 44)], BOLD, head=10)
