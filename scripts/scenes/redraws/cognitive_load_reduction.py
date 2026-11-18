from geometry import BOLD, EDGE
from scenes.redraws._w3 import accessibility_phone, printed_glyph

DESCRIPTION = "A phone presents one expanded task between two closed task rows."


def draw(s):
    face = accessibility_phone(s)
    for v, h in ((59, 12), (26, 30), (11, 12)):
        face.rect(8, v, 31, h, 3, EDGE)
        face.rules(13, v + h - 6, [13], ink=BOLD if h == 30 else EDGE)
        printed_glyph(face, "down" if h == 30 else "arrow", 33, v + h - 6, 3)
    face.rules(13, 43, [20])
    face.rect(13, 31, 13, 7, 2)
