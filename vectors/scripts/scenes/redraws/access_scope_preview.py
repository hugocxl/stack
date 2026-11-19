from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import magnifier
from scenes.redraws._w5 import key_mark, panel

DESCRIPTION = "A permissions card has a key heading and a magnifying glass over its allowed and restricted rows."


def draw(s):
    face = lambda x, z: (x, -.16 * z, z)
    panel(s, rounded(0, 0, 73, 48, 5), face, 6)
    key_mark(s, face, 14, 34, .73, angle=18)
    for z, length, mark in ((22, 27, "check"), (12, 21, "minus")):
        s.line([face(11, z), face(11 + length, z)], EDGE)
        glyph(s, mark, *face(52, z), 6.5, EDGE)
    s.line([face(12, 17), face(43, 17)], DETAIL)
    x, y, z = face(54, 17)
    magnifier(s, x, y + 2, z, 17, direction=(.95, -.31))
