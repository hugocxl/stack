from geometry import BOLD
from scenes.redraws._kit import glyph

DESCRIPTION = "Three bars stand over positive, neutral and negative feedback symbols on their shared base."


def draw(s):
    s.box(0, 0, 0, 96, 33, 18, 3)
    for x, height, kind in ((16, 53, "plus"), (48, 33, "dot"), (80, 20, "minus")):
        s.box(x - 10, 7, 18, 20, 20, height, 1.6)
        glyph(s, kind, x, 33, 9, 7 if kind != "dot" else 11, BOLD)
