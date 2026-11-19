from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import currency_mark, panel, printed_stroke

DESCRIPTION = "A sealed payment envelope has a storefront stamp and an outward arrow beside its currency mark."


def draw(s):
    face = lambda x, z: (x + .3 * z, -.16 * x - .25 * z, z)
    panel(s, rounded(0, 0, 74, 48, 2), face, 3.5)
    printed_stroke(s, face, [(1, 45), (34, 23), (73, 45)], EDGE)
    printed_stroke(s, face, [(2, 2), (24, 30)], DETAIL)
    printed_stroke(s, face, [(72, 2), (52, 33)], DETAIL)
    stamp = lambda x, z: (face(x, z)[0], face(x, z)[1] + .4, z)
    panel(s, rounded(50, 27, 19, 17, 1.8), stamp, .8)
    printed_stroke(s, stamp, [(53, 36), (55, 40), (64, 40), (66, 36),
                              (53, 36), (55, 36), (55, 30), (64, 30),
                              (64, 36)], EDGE)
    currency_mark(s, face, 26, 12, 6)
    glyph(s, "arrow", *face(44, 12), 11, BOLD)
