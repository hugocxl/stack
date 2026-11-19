from geometry import DETAIL
from scenes.redraws._w5 import handled_food_bag

DESCRIPTION = "A handled delivery bag waits on a cantilevered ledge attached to a tall service counter."


def draw(s):
    s.box(0, 0, 0, 61, 24, 50, 2)
    s.box(-2, -1, 48, 65, 27, 5, 2)
    for x in (9, 47):
        s.face([(x, 25, 24), (x, 40, 34), (x, 25, 34)], DETAIL)
    s.box(4, 23, 33, 53, 19, 4, 2)
    handled_food_bag(s, 19, 26, 37, scale=.6)
