from scenes.redraws._kit import badge
from scenes.redraws._w5 import ruled_file

DESCRIPTION = "A ruled document carries a refresh badge at its lower right corner as it is restored."


def draw(s):
    face = ruled_file(s)
    badge(s, "refresh", *face(48, 23), 13)
