from scenes.redraws._kit import badge
from scenes.redraws._w5 import agreement

DESCRIPTION = "A signed contract carries a clock badge at the end of the signature line."


def draw(s):
    face, _ = agreement(s)
    badge(s, "clock", *face(57, 9), 12)
