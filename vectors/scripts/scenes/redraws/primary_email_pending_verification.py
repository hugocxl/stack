from scenes.redraws._kit import badge
from scenes.redraws._w1 import envelope

DESCRIPTION = "A sealed envelope carries a clock badge at its upper corner."


def draw(s):
    envelope(s, -36, 0, 0, 72, 46)
    badge(s, "clock", 36, 0, 42, 13)
