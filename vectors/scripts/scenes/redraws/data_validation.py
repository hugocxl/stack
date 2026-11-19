from scenes.redraws._kit import badge
from scenes.redraws._w2 import grid_table

DESCRIPTION = "A check badge overlaps the lower corner of a populated data table."


def draw(s):
    grid_table(s)
    badge(s, "check", 102, 5, 23, 15)
