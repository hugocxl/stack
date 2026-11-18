from scenes.redraws._kit import badge
from scenes.redraws._w1 import certificate

DESCRIPTION = "A circular arrow badge joins two overlapping certificates with ribbon seals."


def draw(s):
    certificate(s, -19, -12, 9)
    certificate(s, -44, 3, 0)
    badge(s, "refresh", 33, 1, 37, 13)
