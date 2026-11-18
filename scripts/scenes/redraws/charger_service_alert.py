from scenes.redraws._kit import warning
from scenes.redraws._w5 import charger

DESCRIPTION = "An EV charging pedestal carries a warning triangle beside its socket and coiled cable."


def draw(s):
    charger(s)
    warning(s, 33, 16, 28, 24)
