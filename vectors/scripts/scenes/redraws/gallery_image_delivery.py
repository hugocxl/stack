from scenes.redraws._kit import badge
from scenes.redraws._w4 import photograph

DESCRIPTION = "A landscape photograph has an outward arrow badge attached to its right edge."


def draw(s):
    page = photograph(s)
    badge(s, "arrow", *page.at(93, 20), 16)
