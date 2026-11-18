from scenes.redraws._kit import badge
from scenes.redraws._w5 import ruled_file

DESCRIPTION = "A folded-corner file carries a right-pointing move arrow at its edge."


def draw(s):
    face = ruled_file(s)
    badge(s, "arrow", *face(48, 23), 13)
