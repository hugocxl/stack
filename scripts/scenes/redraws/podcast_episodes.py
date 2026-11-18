from scenes.redraws._kit import badge
from scenes.redraws._w4 import broadcast_mic

DESCRIPTION = "A broadcast microphone on a weighted stand carries a play badge on its base."


def draw(s):
    broadcast_mic(s)
    badge(s, "play", 17, 4, 9, 16)
