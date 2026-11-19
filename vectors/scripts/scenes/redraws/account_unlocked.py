from scenes.redraws._kit import badge
from scenes.redraws._w1 import profile_card

DESCRIPTION = "A profile card carries an open padlock badge at its upper corner."


def draw(s):
    profile_card(s, -34, 0, 0)
    badge(s, "unlock", 34, 0, 44, 12)
