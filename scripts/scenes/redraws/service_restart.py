from scenes.redraws._kit import badge
from scenes.redraws._w1 import server_tower

DESCRIPTION = "A refresh badge overlaps the upper-right corner of a server tower."


def draw(s):
    server_tower(s)
    badge(s, "refresh", 25, -3, 60, 12)
