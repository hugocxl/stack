from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w5 import currency_mark, printed_stroke, rect

DESCRIPTION = "A desktop pricing display compares three outlined plan columns, each with a prominent currency price and two feature rows."


def draw(s):
    s.box(29, -16, 0, 35, 29, 4, 3)
    s.box(40, -9, 3, 13, 9, 21, 2)
    s.box(0, -10, 17, 94, 9, 56, 3.8)
    face = lambda x, z: (x, -1, z)
    rect(s, face, 4, 22, 86, 46, 2.2)
    for x, amount, lines in ((8, 5, (13, 9)), (35, 7, (16, 14)), (62, 9, (18, 16))):
        rect(s, face, x, 26, 24, 37, 1.5, DETAIL)
        currency_mark(s, face, x + 7, 52, 5.4, ink=BOLD if x == 35 else EDGE)
        printed_stroke(s, face, [(x + 12, 52), (x + 12 + amount, 52)], EDGE)
        printed_stroke(s, face, [(x + 3, 44), (x + 21, 44)], DETAIL)
        for z, length in zip((37, 31), lines):
            printed_stroke(s, face, [(x + 4, z), (x + 4 + length, z)], EDGE)
