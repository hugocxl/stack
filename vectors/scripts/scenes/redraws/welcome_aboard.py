from geometry import DETAIL, EDGE
from scenes.systems_shapes import rectangle

DESCRIPTION = "An open door swings beside a rectangular welcome mat at the threshold."


def draw(s):
    s.box(-23, -9, 0, 46, 9, 2, 1)
    s.box(-17, 7, 0, 37, 24, 2, 2)
    rectangle(s, -14, 10, 2, 31, 18, DETAIL, 1.5)
    s.box(-28, -9, 0, 5, 9, 59, 1)
    s.box(23, -9, 0, 5, 9, 59, 1)
    s.box(-28, -9, 59, 56, 9, 6, 1)

    def door(u, z):
        return -23 + 12 * u, 41 * u, z

    s.face([door(u, z) for u, z in ((0, 2), (1, 2), (1, 57), (0, 57))], EDGE)
    s.line([door(u, z) for u, z in ((.17, 9), (.83, 9), (.83, 50),
                                   (.17, 50), (.17, 9))], DETAIL)
    s.tube([door(.85, 29), door(.94, 29)], 1.2)
