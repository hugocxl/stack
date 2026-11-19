from geometry import BOLD, EDGE
from scenes.redraws._w3 import ticket

DESCRIPTION = "A notched admission ticket shows a ring sculpture on a pedestal beside a perforated stub."


def draw(s):
    face = ticket(s, depth=5)
    face.rect(23, 7, 27, 7, 1, EDGE)
    face.oval(36, 27, 13, 13, BOLD)
    face.oval(37, 27, 7, 8, EDGE)
    face.stroke([(17, 10), (12, 10)])
    face.stroke([(56, 10), (62, 10)])
