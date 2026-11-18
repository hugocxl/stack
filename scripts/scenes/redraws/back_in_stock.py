from scenes.redraws._kit import badge
from scenes.redraws._w1 import stock_shelf

DESCRIPTION = "A check badge marks a freshly stocked bay on a two-tier inventory shelf."


def draw(s):
    stock_shelf(s, empty=((0, 1),))
    badge(s, "check", -23, 23, 8, 9)
