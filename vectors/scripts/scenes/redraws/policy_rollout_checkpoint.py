from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w5 import policy_book, rect

DESCRIPTION = "A bound policy checklist has an outlined milestone row ending in a check badge."


def draw(s):
    face = policy_book(s)
    for z, length in ((39, 22), (28, 18), (17, 24)):
        rect(s, face, 14, z - 2.8, 6, 5.6, .7, DETAIL)
        s.line([face(25, z), face(25 + length, z)], DETAIL)
    glyph(s, "check", *face(17, 39), 3.5, EDGE)
    rect(s, face, 11, 23, 39, 10, 1.2, EDGE)
    badge(s, "check", *face(53, 28), 11)
