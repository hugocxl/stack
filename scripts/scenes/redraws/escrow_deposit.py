from scenes.redraws._kit import badge
from scenes.redraws._w5 import money_coin

DESCRIPTION = "A thick currency coin carries a lock badge attached to its lower edge."


def draw(s):
    money_coin(s, 0, 0, 29, 29)
    badge(s, "lock", 25, 1, 13, 13)
