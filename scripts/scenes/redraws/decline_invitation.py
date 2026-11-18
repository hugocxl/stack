from scenes.redraws._kit import badge
from scenes.redraws._w1 import envelope

DESCRIPTION = "A sealed invitation envelope carries an X badge at its lower corner."


def draw(s):
    envelope(s, -34, 0, 0, 68, 43)
    badge(s, "x", 35, 0, 12, 13)
