from scenes.redraws._kit import badge
from scenes.redraws._w1 import insulated_cooler

DESCRIPTION = "An insulated shipping cooler carries a right-pointing transfer badge near its upper corner."


def draw(s):
    insulated_cooler(s)
    badge(s, "arrow", 33, -16, 44, 12)
