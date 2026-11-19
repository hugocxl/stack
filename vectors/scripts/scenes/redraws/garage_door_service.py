from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import Surface, wrench_mark

DESCRIPTION = "An open-jaw wrench overlaps the lower corner of a four-panel sectional garage door."


def draw(s):
    s.box(0, -21, 0, 99, 21, 72, 2)
    s.line([(6, 0, 1), (6, 0, 63), (93, 0, 63), (93, 0, 1)], EDGE)
    for z in (16, 31, 46):
        s.line([(7, 0, z), (92, 0, z)], EDGE)
    for x in (15, 40, 65):
        s.face([(x, 0, 51), (x + 18, 0, 51),
                (x + 18, 0, 59), (x, 0, 59)], DETAIL)
    s.line([(44, 0, 7), (56, 0, 7)], DETAIL)

    class WrenchFace(Surface):
        def outline(self, points, ink):
            self.slab(points, 2.6, ink)

    def point(u, v):
        return 91 + .77*u, 10 - .23*u, 14 + v

    wrench_mark(WrenchFace(s, point), 0, 0, 1.13, BOLD)
