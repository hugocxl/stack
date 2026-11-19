from scenes.redraws._kit import badge
from scenes.redraws._w1 import profile_card

DESCRIPTION = "An X badge sits at the upper corner of a profile card's portrait."


def draw(s):
    profile_card(s, -34, 7, 0)
    badge(s, "x", -29, 7, 41, 11)
