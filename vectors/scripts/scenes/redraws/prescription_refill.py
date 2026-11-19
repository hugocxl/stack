from geometry import BOLD
from scenes.redraws._kit import glyph
from scenes.redraws._w4 import pharmacy_bottle

DESCRIPTION = "A capped prescription bottle has a circular refill arrow printed on its wraparound label."


def draw(s):
    label = pharmacy_bottle(s, 0, 0, 0, 1.6)
    glyph(s, "refresh", *label.at(0, 22), 22, BOLD)
