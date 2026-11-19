from scenes.redraws._kit import badge
from scenes.redraws._w5 import sealed_delivery_envelope

DESCRIPTION = "A sealed envelope carries a circular retry arrow on its right corner."


def draw(s):
    sealed_delivery_envelope(s)
    badge(s, "refresh", 65, -2, 10, 12.2)
