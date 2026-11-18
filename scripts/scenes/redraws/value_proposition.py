from geometry import BOLD, EDGE
from scenes.redraws._w4 import printed_glyph, standing_card

DESCRIPTION = "A thick product benefit card pairs a prominent checkmark with its lead line of copy."


def draw(s):
    face = standing_card(s, 98, 62, angle=9, lean=.59, depth=9)
    face.frame(9, 21, 35, 31, 5, EDGE)
    printed_glyph(face, "check", 26.5, 36.5, 17, BOLD)
    face.rows(52, 44, (35,), ink=EDGE)
    face.rows(52, 34, (29, 33), step=-7)
    face.line([(9, 14), (88, 14)])
