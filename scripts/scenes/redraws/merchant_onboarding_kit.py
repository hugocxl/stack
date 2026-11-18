from geometry import DETAIL, EDGE
from scenes.redraws._w1 import open_carton_back, open_carton_front
from scenes.systems_shapes import bezel

DESCRIPTION = "A setup booklet peeks out of an open starter carton stamped with a storefront."


def draw(s):
    carton = (-32, 32, -22, 23, 34)
    open_carton_back(s, *carton)
    s.box(-20, -11, 18, 40, 6, 44, 2)
    s.line([(-15, -5, 33), (-15, -5, 59)], DETAIL)
    for height, width in ((51, 18), (44, 23)):
        s.line([(-9, -5, height), (-9 + width, -5, height)], DETAIL)
    open_carton_front(s, *carton, flap_depth=11, flap_drop=1)

    s.line([(-13, 23, 7), (-13, 23, 18), (-10, 23, 25), (10, 23, 25),
            (13, 23, 18), (13, 23, 7), (-13, 23, 7)], EDGE)
    s.line([(-13, 23, 18), (13, 23, 18)], EDGE)
    for x in (-4, 4):
        s.line([(x * .85, 23, 25), (x, 23, 18)], DETAIL)
    bezel(s, -3, 23, 7, 6, 9, DETAIL, .6)
