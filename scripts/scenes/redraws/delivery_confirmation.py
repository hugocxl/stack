from scenes.redraws._kit import badge
from scenes.redraws._w5 import sealed_delivery_envelope

DESCRIPTION = "A sealed envelope with an address block carries a check badge on its right corner."


def draw(s):
    sealed_delivery_envelope(s)
    badge(s, "check", 65, -2, 10, 12.2)
