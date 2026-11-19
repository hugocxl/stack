from geometry import DETAIL, EDGE
from scenes.redraws._w5 import rect

DESCRIPTION = "A thick ruled register shows three aligned processing records across three columns."


def draw(s):
    s.box(0, 0, 0, 10, 65, 52, 3)
    face = lambda x, z: (10, 65 - x, z)
    s.line([face(8, 1), face(8, 51)], DETAIL)
    for z in (13, 27, 41):
        s.tube([(10, 60, z), (9, 65, z), (4, 67, z), (1, 65, z)], 1, EDGE)
    s.line([face(15, 44), face(39, 44)], EDGE)
    rect(s, face, 14, 7, 43, 30, 1.2, EDGE)
    for z in (17, 27):
        s.line([face(14, z), face(57, z)], DETAIL)
    for x in (29, 43):
        s.line([face(x, 7), face(x, 37)], DETAIL)
    for z, widths in ((12, (7, 4, 7)), (22, (5, 7, 5)), (32, (8, 5, 6))):
        for x, width in zip((18, 33, 47), widths):
            s.line([face(x, z), face(x + width, z)], EDGE)
