from scenes.redraws._kit import badge
from scenes.redraws._w1 import index_cards

DESCRIPTION = "A check badge overlaps one corner of a stack of tabbed index cards."


def draw(s):
    index_cards(s)
    badge(s, "check", 40, 0, 23, 14)
