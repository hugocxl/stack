from scenes.redraws._kit import glyph
from scenes.redraws._w1 import profile_card

DESCRIPTION = "A thick profile card has a bold diagonal slash across its portrait."


def draw(s):
    profile_card(s, -34, 5, 0)
    glyph(s, "slash", -15, 5, 23, 20)
