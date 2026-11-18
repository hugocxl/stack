from geometry import DETAIL, EDGE
from scenes.redraws._w2 import outline

DESCRIPTION = "A taped delivery carton sits inside the open door of a parcel locker bank."


def draw(s):
    s.box(0, 0, 0, 78, 29, 79, 1)
    y = 29.4
    hatch = [(29, y, 28), (74, y, 28), (74, y, 52), (29, y, 52)]
    s.face([(29, 13, 28), (74, 13, 28), (74, 13, 52), (29, 13, 52)])
    s.line([(29, y, 28), (29, 13, 28), (74, 13, 28)], DETAIL)
    s.box(40, 16, 28, 24, 13, 18, 1)
    for x in (48, 54):
        s.line([(x, 16, 46), (x, 29.2, 46), (x, 29.2, 39)], EDGE)

    # The front skin occludes the edges of the recess while leaving the box visible.
    s.face([(78, 0, 0), (78, y, 0), (78, y, 79), (78, 0, 79)], EDGE)
    s.face([(0, y, 0), (78, y, 0), (78, y, 79), (0, y, 79)], EDGE,
           openings=(hatch,))
    for x, z in ((4, 4), (4, 28), (4, 52), (28, 55), (52, 55), (28, 4), (52, 4)):
        outline(s, x, y, z, 21, 20, 1.5)
        s.line([(x + 13, y, z + 9), (x + 17, y, z + 9)], EDGE)
    s.face([(29, y, 28), (42, 61, 28), (42, 61, 52), (29, y, 52)], EDGE)
    s.line([(40, 56, 36), (40, 56, 43)], DETAIL)
