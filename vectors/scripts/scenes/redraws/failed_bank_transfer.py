from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w5 import bank_mark, panel, printed_stroke, ruled_amounts

DESCRIPTION = "A bank-transfer receipt has a bank emblem, a direction arrow, and an attached cross badge."


def draw(s):
    face = lambda x, z: (x, 0, z)
    panel(s, [(0, 2), (53, 2), (53, 62), (0, 62)], face, 3.8)
    bank_mark(s, face, 16, 47, 1.1)
    glyph(s, "arrow", 39, 0, 47, 7, EDGE)
    printed_stroke(s, face, [(6, 33), (46, 33)], DETAIL)
    ruled_amounts(s, face, ((26, 17), (18, 14)), 7, 44, width=9)
    printed_stroke(s, face, [(6, 10), (41, 10)], DETAIL)
    badge(s, "x", *face(50, 8), 10.5)
