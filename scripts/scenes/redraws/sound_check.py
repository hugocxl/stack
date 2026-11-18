from scenes.redraws._kit import badge
from scenes.redraws._w4 import broadcast_mic

DESCRIPTION = "A broadcast microphone carries a check badge at the side of its grille."


def draw(s):
    broadcast_mic(s)
    badge(s, "check", 29, 5, 79, 17)
