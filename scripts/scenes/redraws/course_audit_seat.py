from geometry import EDGE
from scenes.redraws._w3 import cover_cap, eye, ticket

DESCRIPTION = "A course admission ticket pairs a mortarboard heading with an observing-eye mark on the perforated stub."


def draw(s):
    face = ticket(s, marks=False)
    cover_cap(face, 27, 28, 30)
    face.rules(47, 31, [17], ink=EDGE)
    face.rules(47, 21, [14, 17], gap=6)
    eye(face, 84.5, 25, 7.7)
