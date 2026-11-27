from scenes.redraws._kit import warning
from scenes.redraws._w1 import profile_card

DESCRIPTION = "A profile card with a printed avatar carries a warning triangle at its upper corner."


def draw(s):
    profile_card(s, -34, 0, 0)
    warning(s, 34, 0, 34, 26)
