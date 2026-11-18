from geometry import EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w5 import currency_mark, invoice, printed_stroke

DESCRIPTION = "An itemized invoice shows a credit below the total and carries an attached check badge."


def draw(s):
    face = invoice(s)
    x, y, z = face(14, 10)
    glyph(s, "minus", x, y, z, 5.2, EDGE)
    currency_mark(s, face, 24, 10, 5)
    printed_stroke(s, face, [(32, 10), (42, 10)], EDGE)
    badge(s, "check", *face(52, 9), 10.5)
