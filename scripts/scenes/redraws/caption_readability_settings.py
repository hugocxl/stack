from geometry import BOLD, EDGE
from scenes.redraws._w3 import accessibility_phone, printed_glyph

DESCRIPTION = "A phone shows a large sample subtitle above a text-size slider."


def draw(s):
    face = accessibility_phone(s)
    face.rect(8, 30, 31, 42, 2, EDGE)
    printed_glyph(face, "play", 23, 61, 7)
    face.rect(10, 35, 27, 18, 2, EDGE)
    face.rules(13, 47, [21, 15], gap=6, ink=BOLD)
    face.stroke([(11, 19), (35, 19)], EDGE)
    face.rect(25, 15, 8, 8, 4, EDGE)
    face.rules(11, 11, [3])
    face.rules(28, 11, [7])
