from scenes.redraws._kit import badge
from scenes.redraws._w1 import server_tower

DESCRIPTION = "A server tower carries a closed lock badge at its upper status panel."


def draw(s):
    server_tower(s)
    badge(s, "lock", 25, -3, 57, 14)
