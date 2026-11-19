from scenes.redraws._kit import badge
from scenes.redraws._w1 import index_cards

DESCRIPTION = "A circular rebuild arrow badge overlaps one corner of a stack of tabbed index cards."


def draw(s):
    index_cards(s)
    badge(s, "refresh", 40, 0, 23, 14)
