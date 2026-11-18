from geometry import DETAIL, rounded
from scenes.redraws._w5 import panel, rect, train_mark

DESCRIPTION = "A standing rail pass in a desk holder displays a train pictogram above two linked calendar blocks."


def draw(s):
    s.box(1, -14, 0, 54, 25, 8, 3)
    face = lambda x, z: (x, 3 - .17*z, z)
    panel(s, rounded(5, 6, 46, 52, 4), face, 3)
    train_mark(s, face, 28, 41, 1.05)
    for x in (13, 32):
        rect(s, face, x, 13, 12, 12, 1.4)
        s.line([face(x, 21), face(x + 12, 21)], DETAIL)
        for offset in (3, 9):
            s.line([face(x + offset, 23), face(x + offset, 27)], DETAIL)
    s.line([face(26, 18), face(31, 18)], DETAIL)
    s.box(1, 3, 3, 54, 8, 6, 2)
