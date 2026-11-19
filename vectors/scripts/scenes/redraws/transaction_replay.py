from scenes.redraws._kit import badge
from scenes.redraws._w1 import database

DESCRIPTION = "A refresh badge overlaps the top corner of a three-platter database cylinder."


def draw(s):
    database(s, 0, 0, 28, pitch=13)
    badge(s, "refresh", 23, -13, 41, 14)
