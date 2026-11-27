from geometry import BOLD, DETAIL
from scenes.redraws._sf import lip, turned

DESCRIPTION = "Three round columns of different heights compare how three channels perform."


def draw(s):
    for (x, y), h in (((-44, 20), 34), ((0, 0), 74), ((44, -20), 52)):
        turned(s, [(15, 0), (15, h)], x, y, 0, steps=1)
        lip(s, x, y, h, 10, DETAIL, -180, 180)
