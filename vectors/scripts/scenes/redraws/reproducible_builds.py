from geometry import BOLD
from scenes.redraws._w1 import software_package

DESCRIPTION = "An equals sign joins two identical software cartons."


def draw(s):
    software_package(s, -33, 23, 0, .8)
    software_package(s, 33, -23, 0, .8)

    for z in (12, 19):
        s.line([(-5, 5, z), (5, -5, z)], BOLD)
