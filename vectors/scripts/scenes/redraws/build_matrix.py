from geometry import DETAIL, EDGE
from scenes.redraws._w1 import branch
from scenes.systems_shapes import bezel, ring_upright

DESCRIPTION = "A standing build matrix has a source branch above three platform rows and three runtime columns."


def draw(s):
    s.box(-42, -17, 0, 84, 17, 64, 3)
    branch(s, -32, 0, 54, 6)
    bezel(s, -37, 0, 5, 73, 39, EDGE, 1)
    for x in (-19, -1, 17):
        s.line([(x, 0, 5), (x, 0, 44)], DETAIL)
    for z in (17, 29, 39):
        s.line([(-37, 0, z), (36, 0, z)], DETAIL)
    bezel(s, -32, 0, 8, 9, 6, EDGE, 1)
    s.line([(-30, 0, 11), (-25, 0, 11)], DETAIL)
    bezel(s, -30, 0, 19, 5, 8, EDGE, 1)
    bezel(s, -33, 0, 33, 11, 5, EDGE, 1)
    s.line([(-28, 0, 33), (-28, 0, 31)], DETAIL)
    for z in (11, 23, 34):
        for x in (-10, 8, 26):
            ring_upright(s, x, 0, z, 2.1, EDGE)
    for x, length in ((-10, 4), (8, 7), (26, 10)):
        s.line([(x - length / 2, 0, 41.5), (x + length / 2, 0, 41.5)], EDGE)
