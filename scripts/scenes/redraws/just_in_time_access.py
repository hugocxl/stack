from scenes.redraws._kit import badge
from scenes.redraws._w5 import trust_padlock

DESCRIPTION = "A closed access padlock carries an attached clock badge."


def draw(s):
    trust_padlock(s)
    badge(s, "clock", 47, 22, 27, 12)
