from scenes.redraws._kit import badge
from scenes.redraws._w4 import hotel_keycard

DESCRIPTION = "An outward arrow badge overlaps the near corner of a hotel keycard with a magnetic stripe and key emblem."


def draw(s):
    card = hotel_keycard(s)
    badge(s, "arrow", *card.at(95, 63), 14)
