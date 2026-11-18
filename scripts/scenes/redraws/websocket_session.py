from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import browser_header, laptop, server_unit
from scenes.systems_shapes import bezel

DESCRIPTION = "A short cable with opposing arrowheads connects a browser laptop to a server."


def draw(s):
    server_unit(s, 9, -10, width=36, depth=28, height=39)
    y = laptop(s, -48, 6, w=50, h=39, depth=30)
    browser_header(s, -42, y, 34, 38)
    bezel(s, -35, y, 15, 23, 8, EDGE, 1)
    link = [(0, 27, 12), (4, 31, 12), (15, 30, 12),
            (25, 20, 12), (28, 3, 12), (27, -10, 12)]
    s.tube(link, 2.1)
    arrow(s, [(22, 22, 16), (27, 11, 16)], EDGE, head=5.5)
    arrow(s, [(20, 22, 16), (11, 29, 16)], EDGE, head=5.5)
