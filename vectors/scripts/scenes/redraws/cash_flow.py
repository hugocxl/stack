from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import currency_mark, hardback, printed_stroke, ruled_amounts

DESCRIPTION = "A ruled cash-flow statement has a rightward arrow and a dollar sign along its net-cash row."


def draw(s):
    face = hardback(s, 83, 58, depth=9)
    printed_stroke(s, face, [(13, 48), (45, 48)], EDGE)
    ruled_amounts(s, face, ((39, 24), (30, 32)), 13, 73)
    printed_stroke(s, face, [(13, 24), (73, 24)], DETAIL)
    glyph(s, "arrow", 49, 0, 13, 21, BOLD)
    currency_mark(s, face, 19, 13, 6)
