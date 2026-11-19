from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import ticket

DESCRIPTION = "A perforated event ticket has a plus badge on its upper stub corner."


def draw(s):
    face = ticket(s, marks=False)
    face.rules(17, 32, [44], ink=EDGE)
    face.rules(17, 21, [33, 25], gap=7)
    for x in (81, 86, 92, 97):
        face.stroke([(x, 10), (x, 24)], EDGE)
    badge(s, "plus", 104, 0, 47, 12)
