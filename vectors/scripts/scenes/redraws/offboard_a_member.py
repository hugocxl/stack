from scenes.redraws._kit import badge
from scenes.redraws._w1 import profile_card

DESCRIPTION = "A member profile card carries a minus badge at its upper corner."


def draw(s):
    profile_card(s, -34, 0, 0)
    badge(s, "minus", 34, 0, 44, 12)
