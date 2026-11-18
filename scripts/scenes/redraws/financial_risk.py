from scenes.redraws._kit import warning
from scenes.redraws._w5 import money_coin

DESCRIPTION = "A warning triangle overlaps the lower edge of a dollar coin."


def draw(s):
    money_coin(s, 0, 0, 29, 29)
    warning(s, 22, 5, 4, 27)
