from scenes.redraws._kit import badge
from scenes.redraws._w1 import server_tower

DESCRIPTION = "A clock badge marks the top corner of a server instance with two front bays."


def draw(s):
    server_tower(s)
    badge(s, "clock", 25, 1, 49, 15)
