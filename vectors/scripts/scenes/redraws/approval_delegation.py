from scenes.redraws._kit import badge, glyph
from scenes.redraws._w5 import filing_form, rect

DESCRIPTION = "A signed filing form has a checked approval box and an outward arrow badge at its edge."


def draw(s):
    face = filing_form(s)
    rect(s, face, 32, 47, 9, 10, 1.4)
    glyph(s, "check", *face(36.5, 52), 4.9)
    badge(s, "arrow", *face(55, 34), 13)
