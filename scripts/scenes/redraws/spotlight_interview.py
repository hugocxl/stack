from geometry import EDGE, GUIDE
from scenes.redraws._w4 import broadcast_mic

DESCRIPTION = "A broadcast microphone on a desk stand sits under a single cone of stage light."


def draw(s):
    # Draw the beam before the microphone to clear its grille and mount.
    s.ellipse(0, 4, 55, 40, 31, GUIDE, start=-45, end=315)
    for side in (-1, 1):
        s.line([(side*7.8, 4 - side*5.5, 130),
                (side*29, 4 - side*21, 55)], GUIDE)
    s.disk(0, 4, 130, 11, 8, 6, EDGE)
    broadcast_mic(s)
