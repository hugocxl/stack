from scenes.redraws._kit import badge
from scenes.redraws._w1 import profile_card

DESCRIPTION = "Two profile cards stand one behind the other, the front one carrying a check badge."


def draw(s):
    profile_card(s, -22, -24, 0)
    profile_card(s, -40, 0, 0)
    badge(s, "check", 28, 0, 44, 12)
