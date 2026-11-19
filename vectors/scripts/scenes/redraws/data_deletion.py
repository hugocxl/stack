from scenes.redraws._kit import badge
from scenes.redraws._w2 import database

DESCRIPTION = "A three-tier database cylinder carries an X badge at its lower rim."


def draw(s):
    database(s, 0, 30, 45)
    badge(s, "x", 24, -18, 6, 14)
