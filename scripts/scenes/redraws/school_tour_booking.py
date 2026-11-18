from scenes.redraws._kit import badge
from scenes.redraws._w3 import school

DESCRIPTION = "A bell-fronted school has a clock badge beside its double entrance."


def draw(s):
    school(s)
    badge(s, "clock", 86, 51, 13, 14)
