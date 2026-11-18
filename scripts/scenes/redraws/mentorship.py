from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w3 import classroom_chair, flat

DESCRIPTION = "A two-seat study station pairs a tall chair and a short chair at a shared desk with an open workbook."


def draw(s):
    classroom_chair(s, 1, 0, 1.75)
    classroom_chair(s, 48, 3, 1.34)
    # The seats and worktop share a bench frame.
    s.box(4, 12, 9, 65, 4, 4, 1)
    s.box(5, 12, 9, 5, 53, 4, 1)
    s.box(64, 12, 9, 5, 53, 4, 1)
    for x, y in ((5, 39), (65, 39), (5, 61), (65, 61)):
        s.box(x, y, 0, 5, 5, 27, 1)
    s.box(0, 34, 27, 75, 37, 5, 3)
    page = flat(s, 0, 70, 33)
    page.plate([(12, 5), (37, 8), (63, 5), (63, 28), (37, 32), (12, 28)], 2)
    page.stroke([(37, 8), (37, 32)], EDGE)
    page.stroke([(16, 12), (24, 25), (32, 12)], BOLD, closed=True)
    page.rules(44, 23, [13, 9, 10], gap=5, ink=DETAIL)
