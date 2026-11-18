from geometry import DETAIL, EDGE
from scenes.redraws._w1 import status_monitor
from scenes.systems_shapes import bezel

DESCRIPTION = "A desktop monitor shows four staggered trace spans connected in a waterfall."


def draw(s):
    status_monitor(s)
    for x in (-16, 0, 16):
        s.line([(x, 0, 23), (x, 0, 54)], DETAIL, dashed=True)
    for x, z, w in ((-28, 50, 55), (-19, 41, 24), (-7, 32, 31), (9, 23, 18)):
        bezel(s, x, 0, z, w, 4.5, EDGE, 2)
    for x, z, next_x in ((-25, 50, -19), (-16, 41, -7), (-4, 32, 9)):
        s.line([(x, 0, z), (x, 0, z - 6.5), (next_x, 0, z - 6.5)], DETAIL)
