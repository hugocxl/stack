from geometry import EDGE
from scenes.redraws._w1 import database

DESCRIPTION = "A Y-shaped junction links one database cylinder to two matching database shards."


def draw(s):
    root = (-37, -37, 6)
    junction = (-8, -8, 6)
    left, right = (-12, 39, 6), (39, -12, 6)
    s.tube([root, junction, left, junction, right], 2.4, EDGE)
    for x, y, _ in (root, left, right):
        database(s, x, y, 17, pitch=7)
