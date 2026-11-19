from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_line, closed_outline, desktop_monitor, rule

DESCRIPTION = "A plus badge marks the large diamond where a playhead meets a video timeline track."


def draw(s):
    point = desktop_monitor(s, 123, 76)
    for z in (48, 65):
        closed_outline(s, point, rounded(14, z, 95, 13, 1), DETAIL)
    for x in (24, 40, 55, 71, 87, 102):
        chart_line(s, point, [(x, 81), (x, 87)], DETAIL)
    chart_line(s, point, [(62, 36), (62, 85)], EDGE)
    rule(s, point, 16, 55, 91, EDGE)
    diamond = [(62, 70), (77, 55), (62, 40), (47, 55)]
    s.face([point(x, z) for x, z in diamond], BOLD)
    badge(s, "plus", *point(112, 38), 14)
