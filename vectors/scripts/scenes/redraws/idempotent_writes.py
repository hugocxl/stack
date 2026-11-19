from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import database
from scenes.systems_shapes import ring_upright

DESCRIPTION = "Two identical write events converge into a single arrow beside a database cylinder."


def draw(s):
    database(s, 0, 0, 22, pitch=12)
    for z in (5, 39):
        ring_upright(s, -62, 12, z, 4, EDGE)
        s.line([(-58, 12, z), (-51, 12, z), (-44, 12, z * .75 + 5.5),
                (-37, 12, 22)], EDGE)
    arrow(s, [(-37, 12, 22), (-23, 12, 22)], EDGE, head=6)
