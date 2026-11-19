from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import code_brackets, firmware_chip

DESCRIPTION = "An upward arrow badge overlaps the rear corner of a pin-legged firmware chip."


def draw(s):
    firmware_chip(s)
    code_brackets(s, lambda u, v: (u, -v, 15), 14, EDGE)
    badge(s, "up", 24, -24, 22, 14)
