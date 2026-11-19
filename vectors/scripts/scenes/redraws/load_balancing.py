from geometry import EDGE
from scenes.redraws._w1 import server_unit

DESCRIPTION = "A level beam on a central fulcrum distributes one link to three server bays."


def draw(s):
    for x in (-36, -12, 12):
        server_unit(s, x, 10, width=24, depth=22, height=19)
    for x in (-24, 24):
        s.tube([(x, -2, 19), (x, -2, 41)], 1.8)
    s.face([(-10, 1, 20), (0, 1, 42), (10, 1, 20)], EDGE)
    s.box(-33, -6, 42, 66, 10, 5, 2)
    s.tube([(0, -1, 47), (0, -1, 63)], 1.8)
