from scenes.redraws._kit import badge
from scenes.redraws._w1 import open_carton_back, open_carton_front

DESCRIPTION = "An open shipping carton carries a clock badge on its near corner."


def draw(s):
    carton = (-32, 32, -25, 25, 34)
    open_carton_back(s, *carton)
    open_carton_front(s, *carton)
    badge(s, "clock", 47, 21, 34, 14)
