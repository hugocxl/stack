from scenes.redraws._kit import badge
from scenes.redraws._w4 import headset

DESCRIPTION = "A support headset carries a check badge at its right earcup."


def draw(s):
    headset(s)
    badge(s, "check", 44, -8, 23, 12.5)
