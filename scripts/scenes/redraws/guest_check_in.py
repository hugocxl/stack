from scenes.redraws._kit import badge
from scenes.redraws._w4 import hotel_keycard

DESCRIPTION = "A hotel keycard with a magnetic stripe and key emblem carries a check badge at its near corner."


def draw(s):
    card = hotel_keycard(s)
    badge(s, "check", *card.at(95, 63), 14)
