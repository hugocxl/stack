from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import board, chart_line, chart_marker

DESCRIPTION = "A three-step progress line links three large milestones and puts a check badge on the last one."


def draw(s):
    point = board(s, 123, 90, run=.36, rise=.82, level=True)
    milestones = [(19, 21), (58, 43), (100, 65)]
    chart_line(s, point, [(12, 21), milestones[0], (39, 21), (39, 43), milestones[1],
                          (79, 43), (79, 65), milestones[2]], EDGE)
    for x, v in milestones:
        chart_marker(s, point, x, v, 6.2)
    x, y, z = point(100, 65)
    badge(s, "check", x + 7, y - 4, z + 10, 11)
