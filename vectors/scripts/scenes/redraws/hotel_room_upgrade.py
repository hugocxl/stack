from scenes.redraws._kit import badge
from scenes.redraws._w5 import hotel_door

DESCRIPTION = "A hotel door with a bed plaque and a card reader carries an upward-arrow badge."


def draw(s):
    hotel_door(s)
    badge(s, "up", 51, 7, 63, 13)
