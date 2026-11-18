from scenes.redraws._kit import badge
from scenes.redraws._w1 import profile_card

DESCRIPTION = "A plus badge overlaps the upper corner of a profile card beside its portrait."


def draw(s):
    profile_card(s, -34, 0, 0)
    badge(s, "plus", -34, 0, 44, 12)
