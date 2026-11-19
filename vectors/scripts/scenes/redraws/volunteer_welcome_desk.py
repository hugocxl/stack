from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A heart-marked volunteer name badge rests on the ledge of a check-in counter."


def draw(s):
    s.box(1, 4, 0, 91, 41, 47, 4)
    front = Surface(s, (0, 45, 0))
    front.rect(7, 6, 77, 32, 3, DETAIL)
    for x in (12, 20, 28, 36, 44, 52, 60, 68, 76):
        front.stroke([(x, 9), (x, 35)], DETAIL)
    s.box(-3, 0, 46, 99, 51, 6, 3)
    name = Surface(s, (11, 39, 52), rise=(-.44, .89), back=(0, -.89, -.44))
    name.plate(rounded(0, 0, 52, 30, 4), 3, EDGE)
    name.rect(20, 24, 12, 3, 1.4, DETAIL)
    printed_glyph(name, "heart", 12, 15, 9, EDGE)
    name.rules(24, 18, [19], ink=EDGE)
    name.rules(24, 10, [14])
