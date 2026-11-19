from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import currency_mark, open_guide, printed_stroke, ruled_amounts

DESCRIPTION = "An open ledger aligns entries and totals across two facing pages with a check badge beside the matched balance."


def draw(s):
    left, right = open_guide(s)
    for face, x in ((left, 0), (right, 40)):
        currency_mark(s, face, x + 28, 38, 4.4)
        printed_stroke(s, face, [(x + 6, 31), (x + 34, 31)], DETAIL)
        ruled_amounts(s, face, ((25, 9), (18, 10)), x + 6, x + 34, width=8)
        printed_stroke(s, face, [(x + 6, 12), (x + 34, 12)], EDGE)
        printed_stroke(s, face, [(x + 24, 6), (x + 34, 6)], EDGE)
    badge(s, "check", *right(85, 6), 10.5)
