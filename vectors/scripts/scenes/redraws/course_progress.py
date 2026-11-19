from geometry import BOLD, EDGE
from scenes.redraws._w3 import course_card

DESCRIPTION = "A course card has a mortarboard thumbnail and a progress bar hatched to its halfway point."


def draw(s):
    face = course_card(s)
    face.rect(9, 10, 80, 11, 4, EDGE)
    face.stroke([(49, 10), (49, 21)], BOLD)
    for x in range(13, 47, 4):
        face.stroke([(x, 11), (x + 3, 20)], EDGE)
