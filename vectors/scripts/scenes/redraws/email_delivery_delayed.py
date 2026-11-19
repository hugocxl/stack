from scenes.redraws._kit import badge
from scenes.redraws._w5 import sealed_delivery_envelope

DESCRIPTION = "A sealed email envelope carries a clock badge on its lower right corner."


def draw(s):
    sealed_delivery_envelope(s)
    badge(s, "clock", 65, -2, 10, 12.2)
