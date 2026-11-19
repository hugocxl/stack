from scenes.redraws._kit import badge
from scenes.redraws._w3 import photo_art, ticket

DESCRIPTION = "A notched museum admission ticket carries a framed landscape emblem and a crescent badge."


def draw(s):
    face = ticket(s)
    photo_art(face, 14, 8, 42, 31)
    badge(s, "moon", 90, 2, 42, 14)
