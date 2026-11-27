from geometry import DETAIL
from scenes.redraws._sf import lip, open_carton, turned

DESCRIPTION = "A stemmed glass stands upright inside an open shipping carton."


def draw(s):
    front = open_carton(s, -32, -23, 0, 64, 46, 34)
    turned(s, [(9, 4), (9, 5.4), (2, 7), (1.8, 30), (5, 34), (14, 44), (16, 56), (15.5, 64)], 0, 0, 0, steps=4)
    lip(s, 0, 0, 64, 15.5, DETAIL, -180, 180)
    front()
