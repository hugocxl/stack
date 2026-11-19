from geometry import DETAIL, EDGE
from scenes.redraws._w5 import folded_sheet, rect, redaction

DESCRIPTION = "A folded-corner document shows three outlined form fields with only the middle field covered by a dark redaction bar."


def draw(s):
    face = folded_sheet(s, w=53, h=67)
    s.line([face(8, 53), face(30, 53)], EDGE)
    for z, width in ((13, 18), (27, 27), (41, 23)):
        rect(s, face, 8, z - 4.8, 37, 9.6, 1, DETAIL)
        if z == 27:
            redaction(s, face, 12, z - 2.7, width, 5.4)
        else:
            s.line([face(12, z), face(12 + width, z)], EDGE)
