from scenes.redraws._kit import badge
from scenes.redraws._w3 import scholarship

DESCRIPTION = "A mounted scholarship certificate bears a graduation cap, ribbon seal, and clock badge."


def draw(s):
    scholarship(s)
    badge(s, "clock", 104, 1, 72, 14)
