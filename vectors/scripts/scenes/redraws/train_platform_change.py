from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import rect, train_mark

DESCRIPTION = "A station sign shows opposing arrows between two trains with platforms on opposite sides."


def draw(s):
    for x in (2, 72):
        s.box(x, 0, 0, 5, 8, 45, 1)
    s.box(-2, -3, 32, 83, 13, 31, 2.5)
    face = lambda x, z: (x, 10, z)
    rect(s, face, 2, 36, 75, 23, 1.5, DETAIL)
    for x, side in ((17, -1), (63, 1)):
        train_mark(s, face, x, 51, .7, EDGE)
        s.line([face(x + side*8, 43), face(x + side*12, 43),
                face(x + side*12, 39), face(x + side*2, 39)], DETAIL)
    glyph(s, "arrow", 40, 10, 51, 10)
    glyph(s, "back", 40, 10, 43, 10, EDGE)
