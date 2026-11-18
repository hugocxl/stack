from geometry import EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "Three envelopes stand in a queue, and an x badge marks the front envelope."


def draw(s):
    for x, y in ((2, -23), (1, -12), (0, 0)):
        s.box(x - 34, y - 3, 0, 68, 3, 44, 2)
        s.line([(x - 30, y, 39), (x, y, 20), (x + 30, y, 39)], EDGE)

    badge(s, "x", 33, 0, 43, 12)
