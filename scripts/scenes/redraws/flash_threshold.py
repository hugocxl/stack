from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "An oscilloscope shows bright flash pulses rising through a dashed limit line."


def draw(s):
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, 100, 66, 5), 19)
    face.rect(7, 11, 71, 47, 4, EDGE)
    face.stroke([(11, 40), (73, 40)], EDGE, dashed=True)
    face.stroke([(13, 22), (18, 22), (21, 50), (24, 50), (27, 22),
                 (37, 22), (40, 50), (43, 50), (46, 22),
                 (56, 22), (59, 50), (62, 50), (65, 22), (72, 22)], BOLD)
    printed_glyph(face, "bolt", 89, 49, 9, EDGE)
    face.oval(89, 21, 5, 5, DETAIL)
