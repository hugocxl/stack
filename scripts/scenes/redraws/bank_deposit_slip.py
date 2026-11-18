from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import bank_mark, currency_mark, folded_sheet, printed_stroke, rect, ruled_amounts

DESCRIPTION = "A bank deposit slip has an engraved bank heading and a down badge beside its prominent boxed total."


def draw(s):
    face = folded_sheet(s, 75, 47, lean=.32, fold=8)
    bank_mark(s, face, 18, 34, 1.05)
    printed_stroke(s, face, [(34, 38), (61, 38)], EDGE)
    printed_stroke(s, face, [(34, 32), (55, 32)], DETAIL)
    ruled_amounts(s, face, ((24, 24), (18, 18)), 8, 65, width=13)
    rect(s, face, 8, 3, 51, 11, 1.3, EDGE)
    currency_mark(s, face, 24, 8.5, 4.7)
    printed_stroke(s, face, [(33, 8.5), (53, 8.5)], EDGE)
    badge(s, "down", *face(70, 11), 11.5)
