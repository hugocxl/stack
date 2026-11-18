from geometry import DETAIL, EDGE
from scenes.redraws._w1 import prompt
from scenes.systems_shapes import bezel, ring_upright

DESCRIPTION = "A request terminal lists two endpoint rows keyed by one dot and two dots."


def draw(s):
    s.box(-36, -18, 0, 72, 18, 53, 4)
    prompt(s, -27, 0, 41, 4)
    s.line([(-9, 0, 39), (14, 0, 39)], DETAIL)
    for z, dots in ((24, (18,)), (9, (18, 25))):
        bezel(s, -29, 0, z - 4, 58, 11, EDGE, 2)
        s.line([(-22, 0, z - 1), (-18, 0, z + 4)], EDGE)
        s.line([(-13, 0, z + 1), (8, 0, z + 1)], EDGE)
        for x in dots:
            ring_upright(s, x, 0, z + 1, 2, EDGE)
