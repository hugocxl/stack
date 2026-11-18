from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph, warning
from scenes.redraws._w5 import hardback, rect

DESCRIPTION = "A bound policy checklist carries a warning triangle at its lower corner."


def draw(s):
    face = hardback(s, 54, 66)
    s.line([face(13, 54), face(42, 54)], EDGE)
    for z, width in ((40, 22), (28, 25), (16, 19)):
        rect(s, face, 13, z - 3.5, 7, 7, .8, DETAIL)
        s.line([face(25, z), face(25 + width, z)], DETAIL)
    glyph(s, "check", *face(16.5, 40), 4.5, EDGE)
    glyph(s, "check", *face(16.5, 28), 4.5, EDGE)
    warning(s, 49, 2, 6, 26)
