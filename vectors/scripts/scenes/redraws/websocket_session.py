from geometry import EDGE
from scenes.redraws._sf import display, server

DESCRIPTION = "A display and a server are joined by one cable with arrowheads at both ends."


def draw(s):
    display(s, 64, 42, -96, 10, 0)
    s.tube([(-30, 20, 10), (34, 20, 10)], 2, EDGE)
    for x, d in ((-26, -1), (30, 1)):
        s.line([(x + d*6, 14, 10), (x + d*12, 20, 10), (x + d*6, 26, 10)], EDGE)
    server(s, 40, 2, 0, 48, 34, 18)
    server(s, 40, 2, 18, 48, 34, 18)
