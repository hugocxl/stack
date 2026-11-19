from scenes.redraws._kit import badge
from scenes.redraws._w4 import broadcast_mic

DESCRIPTION = "A broadcast microphone on a weighted stand carries an attached clock badge."


def draw(s):
    broadcast_mic(s)
    badge(s, "clock", 44, 7, 57, 16)
