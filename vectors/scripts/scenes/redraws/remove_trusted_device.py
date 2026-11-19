from scenes.redraws._kit import badge
from scenes.redraws._w1 import smartphone

DESCRIPTION = "A standing smartphone carries an X badge beside the upper corner of its screen."


def draw(s):
    smartphone(s)
    badge(s, "x", 15, 4, 38, 8.5)
