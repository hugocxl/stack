from scenes.redraws._kit import badge
from scenes.redraws._w4 import publication

DESCRIPTION = "A folded newspaper carries a circular history arrow badge at its upper corner."


def draw(s):
    page = publication(s)
    badge(s, "refresh", *page.at(75, 12), 15)
