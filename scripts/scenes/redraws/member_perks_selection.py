from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import clipboard, printed_glyph

DESCRIPTION = "A benefits clipboard lists three perk pictograms, with a check badge aligned to the middle row."


def draw(s):
    face = clipboard(s, w=71, h=90)
    for kind, v in (("star", 61), ("heart", 41), ("bolt", 21)):
        printed_glyph(face, kind, 21, v, 8)
        face.rules(34, v + 3, [24], ink=EDGE)
        face.rules(34, v - 4, [17])
    for v in (51, 31):
        face.rules(12, v, [46])
    badge(s, "check", *face.point(66, 41, -2), 9.5)
