from scenes.redraws._kit import badge
from scenes.redraws._w5 import baggage_scale

DESCRIPTION = "An upright suitcase rests on a baggage scale with a check badge beside its readout."


def draw(s):
    baggage_scale(s)
    badge(s, "check", 48, 35, -4, 12)
