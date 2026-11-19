from geometry import BOLD, DETAIL, rounded
from scenes.redraws._w5 import currency_mark, lens_outline, printed_stroke, van

DESCRIPTION = "A delivery van carries a large banknote emblem on its cargo door."


def draw(s):
    van(s)
    face = lambda x, z: (x, 34.1, z)
    s.face([face(x, z) for x, z in rounded(12, 19, 34, 22, 2)])
    lens_outline(s, face, 29, 29.5, 7.4)
    currency_mark(s, face, 29, 29.5, 4.8, ink=BOLD)
    for x in (16.5, 39.5):
        printed_stroke(s, face, [(x, 29.5), (x + 2.8, 29.5)], DETAIL)
