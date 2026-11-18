from scenes.redraws._kit import badge
from scenes.redraws._w5 import charger

DESCRIPTION = "An EV charging pedestal carries a check badge beside its socket and coiled cable."


def draw(s):
    charger(s)
    badge(s, "check", 30, 15, 35, 10.8)
