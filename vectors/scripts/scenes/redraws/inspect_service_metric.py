from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import axes, chart_line, chart_marker, desktop_monitor, face_magnifier

DESCRIPTION = "A magnifier centers on the peak of a single service-metric plot displayed on a desktop monitor."


def draw(s):
    point = desktop_monitor(s, 120, 81)
    axes(s, point, x=12, y=33, width=94, height=53)
    for z in (49, 66, 83):
        s.line([point(13, z), point(105, z)], DETAIL)
    chart_line(s, point, [(16, 42), (34, 56), (49, 53),
                         (74, 75), (92, 59), (103, 64)], EDGE)
    chart_marker(s, point, 74, 75, 4.1, BOLD)
    face_magnifier(s, point, 74, 75, 16, direction=(.79, -.61))
