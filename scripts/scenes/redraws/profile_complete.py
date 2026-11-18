from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w1 import profile_card

DESCRIPTION = "A profile card displays a portrait and three checked detail lines with a large check badge on its corner."


def draw(s):
    profile_card(s, -34, 0, 0, rows=())
    for height, width in ((30, 16), (21, 13), (12, 17)):
        glyph(s, "check", 4, 0, height, 3.3, EDGE)
        s.line([(10, 0, height), (10 + width, 0, height)], DETAIL)
    badge(s, "check", 34, 0, 44, 14)
