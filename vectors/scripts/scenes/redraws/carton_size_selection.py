from scenes.redraws._kit import badge
from scenes.redraws._sf import carton

DESCRIPTION = "Three cartons step up in size, and the middle one carries a check badge."


def draw(s):
    carton(s, -76, 0, 0, 30, 24, 22)
    carton(s, -34, -6, 0, 42, 32, 32)
    carton(s, 20, -14, 0, 56, 42, 44)
    badge(s, "check", 8, 26, 30, 11)
