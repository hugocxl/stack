from scenes.redraws._kit import badge
from scenes.redraws._w5 import sealed_delivery_envelope

DESCRIPTION = "A sealed envelope carries a downward receive arrow badge on its upper edge."


def draw(s):
    sealed_delivery_envelope(s)
    badge(s, "down", 34, -27, 46, 12.8)
