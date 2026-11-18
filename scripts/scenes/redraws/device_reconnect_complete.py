from geometry import EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w5 import device

DESCRIPTION = "An upright phone shows a wireless signal on its screen and carries a check badge on its lower corner."


def draw(s):
    face = device(s, w=43, h=66)
    x, y, z = face(21.5, 33)
    glyph(s, "wifi", x, y, z, 19, EDGE)
    badge(s, "check", 42, -1, 13, 11.8)
