from scenes.redraws._kit import badge
from scenes.redraws._w3 import classroom_chair, classroom_desk

DESCRIPTION = "A school desk and chair carry a plus badge for an adjusted setup."


def draw(s):
    classroom_desk(s, -30, -24, 2)
    classroom_chair(s, -14, 26, 1.8)
    badge(s, "plus", 30, 20, 50, 12)
