from geometry import BOLD, DETAIL, rounded
from scenes.redraws._w5 import panel, rect, train_mark

DESCRIPTION = "A folded expense form has ruled fields and a notched rail ticket clipped to its fare line."


def draw(s):
    sheet = lambda x, z: (x, -z*.42, z)
    s.face([(0, 0, 0), (0, -19, 0), sheet(0, 58)], DETAIL)
    s.face([(0, -19, 0), (56, -19, 0), sheet(56, 58), sheet(0, 58)], DETAIL)
    panel(s, rounded(0, 0, 56, 58, 1.8), sheet, 2)
    rect(s, sheet, 6, 41, 44, 11, 1, DETAIL)
    s.line([sheet(10, 47), sheet(32, 47)], DETAIL)
    for z in (34, 12):
        rect(s, sheet, 6, z, 44, 7, .7, DETAIL)
        s.line([sheet(32, z), sheet(32, z + 7)], DETAIL)
    s.line([sheet(6, 25), sheet(23, 25)], BOLD)
    face = lambda x, z: (x, 2 - z*.42, z)
    outline = [(24, 15), (59, 15), (59, 21), (56, 24),
               (59, 27), (59, 33), (24, 33), (24, 27), (27, 24), (24, 21)]
    s.face([face(x, z) for x, z in outline])
    train_mark(s, face, 41, 24.4, .63)
    s.tube([face(30, 31), face(30, 37), face(34, 37), face(34, 29)], .65, DETAIL)
