from geometry import EDGE
from scenes.redraws._w3 import Surface, speech_outline

DESCRIPTION = "A moderator shield pin overlaps the corner of a forum speech bubble."


def draw(s):
    bubble = Surface(s, (0, 0, 0), rise=(-.15, .98), back=(0, -.98, -.15))
    bubble.plate(speech_outline(0, 9, 83, 58), 7)
    bubble.rules(13, 49, [38, 31, 22], gap=10, ink=EDGE)
    pin = Surface(s, (0, 7, 0))
    pin.plate([(72, 41), (93, 34), (93, 20), (89, 9), (82, 3), (72, -3),
               (62, 3), (55, 9), (51, 20), (51, 34)], 4)
    pin.stroke([(72, 34), (86, 29), (86, 20), (83, 12), (72, 4), (61, 12),
                (58, 20), (58, 29)], EDGE, closed=True)
