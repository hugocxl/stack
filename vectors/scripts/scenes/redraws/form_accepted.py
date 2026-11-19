from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import filing_form, rect

DESCRIPTION = "A filled form with a signature carries a check badge on its lower-right corner."


def draw(s):
    face = filing_form(s)
    rect(s, face, 9, 7, 36, 12, 1, DETAIL)
    s.line([face(9, 60), face(32, 60)], EDGE)
    badge(s, "check", *face(55, 8), 12)
