from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_line, chart_marker, filmstrip

DESCRIPTION = "A filmstrip contains two landscape clips with a star badge marking the second one."


def draw(s):
    point = filmstrip(s, gap=6)
    chart_line(s, point, [(11, 22), (23, 36), (30, 28), (40, 38), (53, 25)], EDGE)
    chart_marker(s, point, 38, 44, 4, EDGE)
    chart_line(s, point, [(62, 22), (75, 29), (86, 27), (98, 37), (108, 30)], EDGE)
    chart_marker(s, point, 77, 44, 4, EDGE)
    badge(s, "star", *point(112, 57), 12)
