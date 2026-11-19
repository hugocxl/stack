from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "An email contact card has an envelope emblem, an address field, and a corner plus badge."


def draw(s):
    s.box(-36, -7, 0, 72, 7, 42, 3)
    bezel(s, -28, 0, 13, 22, 16, EDGE, 1.5)
    s.line([(-27, 0, 28), (-17, 0, 21), (-7, 0, 28)], EDGE)
    bezel(s, 0, 0, 16, 27, 10, EDGE, 1.5)
    s.line([(4, 0, 21), (22, 0, 21)], DETAIL)
    badge(s, "plus", 36, 0, 42, 12)
