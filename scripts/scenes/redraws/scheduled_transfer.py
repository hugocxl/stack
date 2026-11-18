from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w5 import bank_mark, currency_mark, panel, printed_stroke

DESCRIPTION = "A bank-transfer instruction card pairs two bank emblems with a transfer arrow, a currency amount, and an attached clock badge."


def draw(s):
    face = lambda x, z: (x, -.54 * z, z)
    panel(s, rounded(0, 0, 82, 49, 4), face, 6)
    for x in (20, 60):
        bank_mark(s, face, x, 32, .92)
    glyph(s, "arrow", *face(40, 32), 9, EDGE)
    printed_stroke(s, face, [(10, 21), (71, 21)], DETAIL)
    currency_mark(s, face, 21, 12, 6, ink=BOLD)
    printed_stroke(s, face, [(31, 12), (61, 12)], EDGE)
    badge(s, "clock", *face(78, 12), 12)
