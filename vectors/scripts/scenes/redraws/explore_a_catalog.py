from geometry import EDGE
from scenes.redraws._w2 import plan_magnifier
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open bound catalog displays four product thumbnails, with a magnifier over the nearest listing."


def draw(s):
    left, right = open_book(s)
    for page, u in ((left, 11), (right, 70)):
        for v in (10, 39):
            page.frame(u, v, 42, 20, 2, EDGE)
            page.rows(u + 3, v + 24, (27,))
    left.oval(32, 20, 6, 6, EDGE)
    left.frame(24, 44, 16, 10, 2, EDGE)
    right.outline([(83, 25), (91, 14), (99, 25)], EDGE)
    right.outline([(87, 49), (95, 41), (103, 49), (95, 57)], EDGE)
    plan_magnifier(s, 100, 48, 23, 16, direction=(.22, .976))
