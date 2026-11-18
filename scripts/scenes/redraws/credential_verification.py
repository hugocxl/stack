from scenes.redraws._kit import badge
from scenes.redraws._w3 import credential

DESCRIPTION = "An academic credential card with a mortarboard seal carries a check badge on its lower corner."


def draw(s):
    face = credential(s)
    badge(s, "check", *face.point(86, 15), 15)
