from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import outline, rule

DESCRIPTION = "A plus badge adds a field to a thick customer record with an ID tab."


def draw(s):
    s.box(0, -20, 0, 102, 20, 72, 5)
    s.box(11, -16, 72, 32, 10, 8, 3)
    outline(s, 11, 0, 44, 28, 17, 3, EDGE)
    s.line([(17, 0, 55), (30, 0, 55)], DETAIL)
    s.line([(17, 0, 50), (24, 0, 50)], DETAIL)
    def point(x, z):
        return x, 0, z

    for x, z, length in ((48, 56, 32), (48, 47, 24), (18, 31, 57), (18, 20, 47), (18, 10, 62)):
        rule(s, point, x, z, length, EDGE if z == 56 else DETAIL)
    for z in (10, 20, 31):
        s.line([(11, 0, z), (13, 0, z)], EDGE)
    badge(s, "plus", 96, 5, 35, 14)
