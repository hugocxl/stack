from geometry import EDGE, rounded
from scenes.redraws._w4 import front_surface

DESCRIPTION = "One home page branches through a shared connector into three smaller pages."


def draw(s):
    face = front_surface(s, angle=-24, z=5, lean=.08)
    face.line([(59, 59), (59, 46)], EDGE)
    face.line([(15, 32), (15, 46), (103, 46), (103, 32)], EDGE)
    face.line([(59, 46), (59, 32)], EDGE)
    for x, z, width, height in ((37, 59, 44, 33), (0, 7, 30, 25),
                                (44, 7, 30, 25), (88, 7, 30, 25)):
        page = rounded(x, z, width, height, 3)
        face.slab(page, 5)
        face.line([(x + 1, z + height - 7), (x + width - 1, z + height - 7)])
        if z == 7:
            face.rows(x + 6, z + 12, (17, 11), step=-6)
        else:
            face.line([(51, 73), (59, 79), (67, 73)], EDGE)
            face.outline([(54, 75), (54, 66), (64, 66), (64, 75)], EDGE)
