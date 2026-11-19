from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import coin_stack, money_coin

DESCRIPTION = "A dollar coin follows a curved arrow from one coin stack to the next."


def draw(s):
    coin_stack(s, 0, 10, 0, 12, 5)
    coin_stack(s, 56, 6, 0, 12, 2)
    arrow(s, [(3, 9, 20), (10, 7, 35), (22, 4, 40), (36, 2, 41),
              (49, 3, 39), (56, 6, 25)], EDGE, head=6)
    money_coin(s, 28, 12, 38, 10)
