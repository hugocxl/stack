from geometry import BOLD, EDGE
from scenes.redraws._w5 import currency_mark, hardback, printed_stroke, rect, ruled_amounts

DESCRIPTION = "A bound credit statement frames a prominent currency balance above two account rows."


def draw(s):
    face = hardback(s, 63, 66, depth=11)
    printed_stroke(s, face, [(14, 56), (38, 56)], EDGE)
    rect(s, face, 14, 28, 42, 21, 2)
    currency_mark(s, face, 25, 38, 7.5, ink=BOLD)
    printed_stroke(s, face, [(36, 38), (49, 38)], EDGE)
    ruled_amounts(s, face, ((19, 16), (11, 20)), 14, 54, width=9)
