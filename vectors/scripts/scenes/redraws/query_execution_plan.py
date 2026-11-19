from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import database, upright_profile
from scenes.systems_shapes import bezel, ring_upright

DESCRIPTION = "An execution tree connects a database root through an intersecting-ring join node to two table scans."


def draw(s):
    s.line([(0, 0, 83), (0, 0, 63)], EDGE)
    s.line([(0, 0, 43), (0, 0, 32)], EDGE)
    s.line([(-34, 0, 20), (-34, 0, 32), (34, 0, 32), (34, 0, 20)], EDGE)
    for x in (-34, 34):
        s.box(x - 16, -8, 0, 32, 8, 21, 2)
        bezel(s, x - 11, 0, 4, 22, 12, EDGE, 1)
        s.line([(x - 11, 0, 11), (x + 11, 0, 11)], DETAIL)
        s.line([(x - 3, 0, 4), (x - 3, 0, 16)], DETAIL)

    join = [(-16, 53), (0, 64), (16, 53), (0, 42)]
    upright_profile(s, join, 0, 5)
    for x in (-4, 4):
        ring_upright(s, x, 0, 53, 5.5, BOLD)
    database(s, 0, 0, 13.5, bottom=81, pitch=5)
