from scenes.redraws._kit import badge
from scenes.redraws._w5 import hotel_door

DESCRIPTION = "A hotel door with a bed plaque and a card reader carries a clock badge."


def draw(s):
    hotel_door(s)
    badge(s, "clock", 51, 7, 63, 13)
