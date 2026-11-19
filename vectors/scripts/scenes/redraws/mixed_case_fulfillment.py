from geometry import DETAIL, EDGE
from scenes.redraws._w1 import open_carton_back, open_carton_front
from scenes.systems_shapes import bezel

DESCRIPTION = "An open shipping carton holds a gable-top case and a lower ribbed case fitted side by side."


def draw(s):
    carton = (-35, 35, -25, 25, 28)
    open_carton_back(s, *carton)

    # The upright case and the low corrugated case share the same packing floor.
    s.box(-30, -19, 0, 27, 34, 41, 1.4)
    s.face([(-30, -19, 41), (-3, -19, 41), (-3, -2, 52), (-30, -2, 52)], DETAIL)
    s.face([(-3, -19, 41), (-3, 15, 41), (-3, -2, 52)], EDGE)
    s.face([(-30, 15, 41), (-3, 15, 41), (-3, -2, 52), (-30, -2, 52)], EDGE)
    s.box(-30, -3, 52, 27, 2, 4, .4)
    bezel(s, -25, 15, 30, 16, 7, DETAIL, .8)

    s.box(0, -19, 0, 30, 34, 34, 1.7)
    for y in (-14, -7, 0, 7):
        s.line([(2, y, 34), (27, y, 34)], DETAIL)
    open_carton_front(s, *carton)
