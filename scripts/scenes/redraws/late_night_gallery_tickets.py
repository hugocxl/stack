from scenes.redraws._kit import badge
from scenes.redraws._w3 import photo_art, ticket

DESCRIPTION = "A crescent moon badge overlaps the stub of a die-cut gallery ticket printed with framed artwork."


def draw(s):
    face = ticket(s, depth=4)
    photo_art(face, 15, 8, 49, 32)
    badge(s, "moon", 94, 3, 43, 14)
