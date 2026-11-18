from geometry import DETAIL
from scenes.redraws._w5 import handled_food_bag

DESCRIPTION = "A shopfront pickup window has a striped awning and a handled food bag in its serving opening."


def draw(s):
    s.box(0, 0, 0, 64, 12, 66, 2)
    s.box(0, 10, 0, 64, 12, 19, 1.5)
    s.box(0, 10, 19, 7, 12, 33, 1)
    s.box(57, 10, 19, 7, 12, 33, 1)
    s.box(2, 13, 19, 60, 13, 4, 1.5)
    handled_food_bag(s, 19, 17, 23, scale=.52)
    s.face([(-3, 10, 68), (66, 10, 68), (66, 29, 60), (-3, 29, 60)])
    s.face([(-3, 29, 60), (66, 29, 60), (66, 29, 56), (-3, 29, 56)])
    for x in (10, 24, 38, 52):
        s.line([(x, 10, 68), (x, 29, 60), (x, 29, 56)], DETAIL)
