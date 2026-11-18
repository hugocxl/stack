from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import magnifier
from scenes.redraws._w5 import audit_sheet, avatar_mark

DESCRIPTION = "A magnifying glass covers the account and lock columns of a punched access log."


def draw(s):
    face = audit_sheet(s)
    for z in (13, 29, 45):
        avatar_mark(s, face, 21, z, .62)
        s.line([face(28, z), face(34, z)], DETAIL)
        glyph(s, "lock", *face(42, z), 5.8, EDGE)
    x, y, z = face(34, 34)
    magnifier(s, x, y + 5, z, 19, direction=(.75, -.66))
