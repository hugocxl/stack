from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import currency_mark, invoice, printed_stroke

DESCRIPTION = "An invoice carries a clock badge beside the amount due below its itemized charges."


def draw(s):
    face = invoice(s)
    currency_mark(s, face, 17, 10, 6, ink=BOLD)
    printed_stroke(s, face, [(27, 10), (42, 10)], EDGE)
    badge(s, "clock", *face(53, 13), 12)
