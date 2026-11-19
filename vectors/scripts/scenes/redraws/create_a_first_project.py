from scenes.redraws._kit import badge
from scenes.redraws._w1 import standing_folder

DESCRIPTION = "A standing project folder carries a plus badge at its raised tab."


def draw(s):
    standing_folder(s)
    badge(s, "plus", -35, -6, 48, 11.5)
