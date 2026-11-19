from scenes.redraws._kit import badge
from scenes.redraws._w1 import envelope

DESCRIPTION = "A sealed invitation envelope carries a check badge at its lower corner."


def draw(s):
    envelope(s, -34, 0, 0, 68, 43)
    badge(s, "check", 35, 0, 12, 13)
