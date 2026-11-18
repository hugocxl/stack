from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import ethernet_port

DESCRIPTION = "A gateway's single inlet follows a branching trace to two outgoing routes."


def draw(s):
    s.box(-28, -23, 0, 56, 46, 18, 2)
    ethernet_port(s, -9, 23, 8, 13, 10)
    arrow(s, [(-9, 53, 8), (-9, 29, 8)], EDGE, head=8)

    top = 18
    s.line([(-9, 23, 8), (-9, 23, top), (-9, 2, top), (3, 2, top)], BOLD)
    for y in (-12, 13):
        s.line([(3, 2, top), (12, y, top), (28, y, top), (28, y, 8)], BOLD)
        s.line([(28, y - 4, 8), (28, y + 4, 8)], DETAIL)
        arrow(s, [(28, y, 8), (50, y, 8)], EDGE, head=8)
