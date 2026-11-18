from scenes.redraws._kit import badge
from scenes.redraws._w4 import publication

DESCRIPTION = "A folded newspaper with a masthead and story grid carries a clock badge at its upper-right corner."


def draw(s):
    page = publication(s)
    badge(s, "clock", *page.at(73, 18), 18)
