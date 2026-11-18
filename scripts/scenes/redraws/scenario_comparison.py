from geometry import EDGE
from scenes.redraws._w2 import axes, board, chart_line, chart_marker

DESCRIPTION = "Two scenario paths share one origin and end at different heights on a single chart."


def draw(s):
    point = board(s, 116, 79, run=.52, rise=.74)
    axes(s, point, width=92, height=58)
    origin = (20, 29)
    chart_line(s, point, [origin, (37, 43), (53, 38), (71, 56), (87, 53), (102, 68)])
    chart_line(s, point, [origin, (37, 23), (54, 27), (72, 20), (88, 28), (102, 33)],
               EDGE, dash=(5, 3))
    for x, v in (origin, (102, 68), (102, 33)):
        chart_marker(s, point, x, v, 3.3)
