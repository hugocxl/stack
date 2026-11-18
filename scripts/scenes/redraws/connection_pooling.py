from geometry import DETAIL, EDGE
from scenes.redraws._w1 import database
from scenes.systems_shapes import bezel

DESCRIPTION = "Three cables enter a shared junction hub, which connects to one database cylinder."


def draw(s):
    database(s, 18, -25, 22, pitch=9)
    s.tube([(18, -4, 12), (18, 4, 12), (11, 11, 12), (1, 14, 12)], 2.6)
    s.box(-31, 6, 0, 49, 22, 19, 3)
    for x, end in ((-22, -32), (-7, -7), (8, 18)):
        bezel(s, x - 4, 28, 5, 8, 8, EDGE, 1)
        s.tube([(x, 28, 9), (x, 35, 9), (end, 43, 7)], 2.1)
    s.line([(-19, 14, 19), (6, 14, 19)], DETAIL)
