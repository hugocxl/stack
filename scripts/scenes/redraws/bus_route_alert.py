from scenes.redraws._kit import warning
from scenes.redraws._w5 import bus

DESCRIPTION = "A city bus carries a warning triangle at the outer corner of its windshield."


def draw(s):
    bus(s)
    warning(s, 84, 14, 29, 27)
