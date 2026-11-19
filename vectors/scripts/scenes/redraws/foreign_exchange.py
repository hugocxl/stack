from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import money_coin

DESCRIPTION = "Two opposing arrows connect a dollar coin and a euro coin."


def draw(s):
    money_coin(s, 69, -10, 25, 23, euro=True)
    money_coin(s, 20, 13, 25, 23)
    arrow(s, [(29, 8, 49), (46, 4, 49), (55, 1, 48)], EDGE, head=6)
    arrow(s, [(61, -8, 2), (45, -1, 2), (36, 2, 3)], EDGE, head=6)
