from scenes.redraws._kit import badge
from scenes.redraws._w1 import memory_chip

DESCRIPTION = "A lightning badge overlaps the corner of a pin-legged cache memory chip."


def draw(s):
    memory_chip(s)
    badge(s, "bolt", 27, -23, 19, 14)
