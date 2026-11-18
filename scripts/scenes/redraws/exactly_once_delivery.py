from scenes.redraws._kit import badge
from scenes.redraws._w1 import envelope

DESCRIPTION = "A single sealed envelope carries one check badge at its corner."


def draw(s):
    envelope(s, -34, 0, 0, width=68, height=44)
    badge(s, "check", 35, 0, 18, 15)
