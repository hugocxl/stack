from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import currency_mark, panel, printed_stroke

DESCRIPTION = "A budget envelope shows a star-marked spending label above its allocated currency amount."


def draw(s):
    face = lambda x, z: (.66 * x - .21 * z, -.74 * x - .16 * z, z)
    panel(s, rounded(0, 0, 65, 48, 2.3), face, 5)
    printed_stroke(s, face, [(2, 46), (32, 26), (63, 46)], EDGE)
    printed_stroke(s, face, [(3, 2), (20, 34)], DETAIL)
    printed_stroke(s, face, [(62, 2), (45, 34)], DETAIL)
    label = lambda x, z: (face(x, z)[0], face(x, z)[1] + .8, z)
    panel(s, rounded(15, 20, 35, 13, 1.5), label, .8, DETAIL)
    glyph(s, "star", *label(22, 26.5), 6, EDGE)
    printed_stroke(s, label, [(30, 26.5), (44, 26.5)], DETAIL)
    currency_mark(s, face, 24, 11, 5.5, ink=BOLD)
    printed_stroke(s, face, [(31, 11), (43, 11)], EDGE)
