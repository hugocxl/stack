from scenes.redraws._kit import badge
from scenes.redraws._w5 import filing_form

DESCRIPTION = "A signed filing form with a folded corner carries a check badge on its right edge."


def draw(s):
    face = filing_form(s)
    badge(s, "check", *face(55, 29), 17)
