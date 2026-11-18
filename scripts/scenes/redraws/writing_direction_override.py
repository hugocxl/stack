from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A long left-pointing arrow heads a paragraph control whose text aligns to the right."


def draw(s):
    control = Surface(s, (0, 0, 0), across=(.16, -.99), back=(-.99, -.16, 0))
    control.plate(rounded(0, 0, 99, 69, 5), 12)
    control.rect(8, 8, 83, 53, 4, EDGE)
    control.rules(8, 42, [83], ink=EDGE)
    printed_glyph(control, "back", 49, 52, 22, BOLD)
    for x, v in ((20, 32), (32, 23), (49, 14)):
        control.rules(x, v, [80 - x], ink=EDGE)
