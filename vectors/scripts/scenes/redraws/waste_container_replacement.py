from scenes.redraws._kit import badge
from scenes.redraws._w1 import wheelie_bin

DESCRIPTION = "A wheeled waste bin with a hinged lid carries a circular-arrow badge."


def draw(s):
    wheelie_bin(s, 0, 0)
    badge(s, "refresh", 30, -2, 45, 13)
