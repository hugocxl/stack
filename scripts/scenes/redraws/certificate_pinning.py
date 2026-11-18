from scenes.redraws._kit import badge
from scenes.redraws._w1 import certificate

DESCRIPTION = "A padlock badge overlaps the ribbon seal on a framed certificate."


def draw(s):
    certificate(s, -34, 0, 0)
    badge(s, "lock", 37, 0, 17, 13)
