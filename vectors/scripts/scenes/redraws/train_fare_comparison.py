from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import rect, train_mark

DESCRIPTION = "A rail fare board shows a train pictogram and two price rows marked with unequal groups of coins."


def draw(s):
    face = lambda x, z: (x, 4, z)
    s.box(2, -11, 0, 68, 15, 55, 4)
    rect(s, face, 6, 7, 60, 42, 1.4, DETAIL)
    train_mark(s, face, 17, 29, .93, BOLD)
    s.line([face(29, 7), face(29, 49)], DETAIL)
    s.line([face(33, 27), face(62, 27)], DETAIL)
    for z, count in ((37, 3), (18, 1)):
        s.line([face(34, z), face(37, z)], EDGE)
        for i in range(count):
            x = 43 + i*8
            s.line([face(a, b) for a, b in oval(x, z, 3.5, 4.3, count=24)], EDGE)
            s.line([face(x, z - 1.6), face(x, z + 1.6)], DETAIL)
