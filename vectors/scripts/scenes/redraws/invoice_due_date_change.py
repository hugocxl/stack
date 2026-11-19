from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import calendar_header, invoice_total, printed_stroke, rect, ruled_amounts, folded_sheet

DESCRIPTION = "A folded-corner invoice has a boxed calendar field with a horizontal change arrow above its itemized amounts."


def draw(s):
    face = folded_sheet(s, 59, 71, lean=.46, fold=11)
    rect(s, face, 6, 43, 47, 16, 2, EDGE)
    calendar_header(s, face, 10, 45, .74)
    printed_stroke(s, face, [(25, 51), (32, 51)], DETAIL)
    glyph(s, "arrow", *face(42, 51), 9.5)
    ruled_amounts(s, face, ((35, 21), (28, 16), (21, 23)), 8, 50)
    printed_stroke(s, face, [(8, 16), (50, 16)], EDGE)
    invoice_total(s, face, z=8, end=50, ink=EDGE)
