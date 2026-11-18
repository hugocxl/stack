from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import ethernet_port, router

DESCRIPTION = "Two matching routers share a directly attached link with an arrowhead in each direction."


def draw(s):
    left, right = (-37, 26), (37, -26)
    s.line([(*left, 8), (*right, 8)], EDGE)
    arrow(s, [(-5, 3, 8), (11, -8, 8)], BOLD, head=8)
    arrow(s, [(5, -3, 8), (-11, 8, 8)], BOLD, head=8)
    for x, y in (right, left):
        router(s, x, y)
        ethernet_port(s, x - 8, y + 13, 8, 10, 8)
        s.line([(x + 4, y + 13, 8), (x + 9, y + 13, 8)], EDGE)
