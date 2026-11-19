from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import chart_line, chart_marker, desktop_monitor

DESCRIPTION = "A leftward rewind arrow points into the earlier part of a performance chart on a monitor."


def draw(s):
    p = desktop_monitor(s, 127, 94)
    s.line([p(13, 95), p(13, 35), p(113, 35)], DETAIL)
    for x in (30, 57, 83, 111):
        s.line([p(x, 35), p(x, 30)], DETAIL)
    past = [(15, 42), (27, 49), (40, 47), (53, 59), (64, 56), (76, 66),
            (88, 62), (100, 73), (111, 77)]
    chart_line(s, p, past, EDGE)
    for x, z in past[::2]:
        chart_marker(s, p, x, z, 3, EDGE)
    arrow(s, [p(104, 84), p(104, 94), p(93, 99), p(36, 99)], BOLD, head=12)
