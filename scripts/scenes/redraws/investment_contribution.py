from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import currency_mark, panel, printed_stroke

DESCRIPTION = "An investment account card shows a rising chart and an attached plus badge."


def draw(s):
    face = lambda x, z: (x, -.38 * z, z)
    panel(s, rounded(0, 0, 59, 57, 4), face, 8)
    currency_mark(s, face, 13, 44, 6)
    printed_stroke(s, face, [(25, 44), (49, 44)], DETAIL)
    printed_stroke(s, face, [(10, 33), (10, 10), (50, 10)], DETAIL)
    printed_stroke(s, face, [(14, 15), (25, 23), (34, 20), (49, 34)], EDGE)
    badge(s, "plus", *face(58, 21), 10.5)
