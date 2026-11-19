from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w5 import access_form, rect

DESCRIPTION = "A key heads a clipboard checklist with a check badge attached to the completed review rows."


def draw(s):
    face = access_form(s)
    for z, length in ((29, 21), (20, 18), (11, 15)):
        rect(s, face, 8, z - 3, 6, 6, .7, DETAIL)
        glyph(s, "check", *face(11, z), 3.3, EDGE)
        s.line([face(19, z), face(19 + length, z)], DETAIL)
    badge(s, "check", *face(44, 18), 10)
