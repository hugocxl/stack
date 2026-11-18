from scenes.redraws._kit import badge
from scenes.redraws._w1 import conveyor, software_package

DESCRIPTION = "Three code packages wait in line on a conveyor beneath a clock badge."


def draw(s):
    conveyor(s, -43, 18, 86, 33)
    for x in (-29, 0, 29):
        software_package(s, x, 1, 19, .39)
    badge(s, "clock", 25, -9, 42, 12)
