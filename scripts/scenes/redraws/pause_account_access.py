from scenes.redraws._kit import badge
from scenes.redraws._w1 import profile_card

DESCRIPTION = "A profile card carries a two-bar pause badge at its upper corner."


def draw(s):
    profile_card(s, -34, 0, 0)
    badge(s, "pause", 34, 0, 44, 12)
