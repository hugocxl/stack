from math import cos, pi

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, chart_marker, landscape_frame

DESCRIPTION = "A split landscape photograph compares hazy mountain contours with a sharply defined ridge."


def draw(s):
    point = landscape_frame(s)
    chart_marker(s, point, 77, 57, 7, EDGE)
    chart_line(s, point, [(55, 40), (68, 49), (88, 28), (95, 36), (102, 29)], EDGE)
    chart_line(s, point, [(62, 45), (66, 43), (68, 46), (73, 44)], DETAIL)
    for lift in (0, 5, 10):
        chart_line(s, point, [(8 + 47*i/24, 25 + lift + 10*(1 - cos(pi*i/12))/2 + 5*i/24)
                              for i in range(25)], DETAIL)
    chart_line(s, point, [(55, 12), (55, 74)], BOLD)
