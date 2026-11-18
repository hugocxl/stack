from geometry import EDGE
from scenes.redraws._w1 import conveyor, package_machine

DESCRIPTION = "A conveyor carries three identical blocks into the open throat of a processing machine."


def draw(s):
    conveyor(s, -38, 13, 79, 27)
    for x in (23, 5, -13):
        s.box(x, -7, 19, 12, 13, 12, 1.4, EDGE)
    package_machine(s, -25, 14, 29)
