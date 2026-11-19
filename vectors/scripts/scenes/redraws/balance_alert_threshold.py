from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import warning
from scenes.redraws._w5 import currency_mark, panel, rect

DESCRIPTION = "A warning triangle overlaps the visible banknote in an open clasp wallet."


def draw(s):
    back = lambda x, z: (x, -10 - z * .11, z)
    panel(s, rounded(0, 0, 69, 46, 6), back, 3.5)

    note = lambda x, z: (x, -5 - z * .19, z)
    panel(s, [(6, 21), (57, 21), (57, 57), (6, 57)], note, 1)
    rect(s, note, 10, 27, 43, 26, 2, DETAIL)
    currency_mark(s, note, 23, 47, 6)

    face = lambda x, z: (x, -z * .09, z)
    panel(s, rounded(0, 0, 69, 35, 6), face, 8)
    rect(s, face, 4, 4, 60, 27, 5, DETAIL)
    clasp = lambda x, z: (x, 2.5 - z * .09, z)
    panel(s, rounded(49, 11, 22, 13, 5), clasp, 2, EDGE)
    rect(s, clasp, 56, 15, 5, 5, 2.4, DETAIL)
    warning(s, 48, -.7, 34, 25)
