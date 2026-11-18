from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import plane_mark

DESCRIPTION = "A two-post airport departure board lines up destination entries with three clock symbols."


def draw(s):
    for x in (8, 70):
        s.box(x, 0, 0, 5, 7, 48, 1)
    s.box(0, 1, 28, 84, 9, 56, 3)
    face = lambda x, z: (x, 10, z)
    plane_mark(s, face, 13, 73, .49, BOLD)
    s.line([face(25, 74), face(72, 74)], EDGE)
    s.line([face(3, 64), face(81, 64)], EDGE)
    s.line([face(59, 31), face(59, 64)], DETAIL)
    for z, width, minute in ((35, 30, 1), (47, 39, -1), (59, 34, .5)):
        s.line([face(11, z), face(11 + width, z)], EDGE)
        s.line([face(x, v) for x, v in oval(70, z, 4.7, 4.7, count=20)], EDGE)
        s.line([face(70, z + 2.8), face(70, z), face(70 + 2.8*minute, z - 1.5)], EDGE)
    for z in (41, 53):
        s.line([face(4, z), face(80, z)], DETAIL)
