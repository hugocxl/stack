from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w5 import currency_mark, printed_stroke

DESCRIPTION = "An alert bell has dollar and euro symbols engraved on its flared body."


def draw(s):
    rx, ry = 29, 12
    face = lambda x, z: (x, -x * (ry / rx) ** 2, z)
    lip = rx ** 2 / (rx ** 2 + ry ** 2) ** .5
    s.tube([face(-4, 58), face(-4, 64), face(0, 67), face(4, 64),
            face(4, 58)], 2)
    s.disk(0, 3, 0, 5, 5, 12)
    outline = [(-lip, 13), (-23, 17), (-20, 22), (-18, 29), (-16, 43),
               (-13, 51), (-8, 57), (0, 59), (8, 57), (13, 51),
               (16, 43), (18, 29), (20, 22), (23, 17), (lip, 13)]
    s.face([face(x, z) for x, z in outline])
    s.disk(0, 0, 9, rx, ry, 4)
    s.ellipse(0, 0, 13, 26.5, 10, DETAIL, start=3, end=92)
    currency_mark(s, face, -9, 34, 7.6, ink=EDGE)
    currency_mark(s, face, 9, 34, 7.6, euro=True, ink=EDGE)
    printed_stroke(s, face, [(-1.6, 27), (1.6, 41)], BOLD)
