from scenes.redraws._kit import badge
from scenes.redraws._w5 import device

DESCRIPTION = "A standing phone and landscape tablet share a check badge at their front corner."


def draw(s):
    device(s, w=62, h=45, tablet=True)
    face = device(s, x=44, y=4, w=32, h=55)
    badge(s, "check", *face(31, 14), 11)
