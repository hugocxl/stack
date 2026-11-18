from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import axes, chart_line, chart_marker, desktop_monitor, response_curve

DESCRIPTION = "A monitor places a single marker on a cumulative curve and projects its height to the percentage scale."


def draw(s):
    p = desktop_monitor(s, 130, 103)
    x0, z0 = 18, 36
    point = lambda x, z: p(x0 + .86*x, z0 + z)
    axes(s, point, x=0, y=0, width=111, height=72)
    for z in (20, 40, 60):
        s.line([point(-5, z), point(0, z)], EDGE)
    chart_line(s, point, [(1, 52), (73, 52), (73, 3)], DETAIL, dash=(4, 3))
    chart_line(s, point, response_curve(), EDGE)
    chart_marker(s, point, 73, 52, 5.8, BOLD)
