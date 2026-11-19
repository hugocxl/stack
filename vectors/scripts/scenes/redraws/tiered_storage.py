from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import platter

DESCRIPTION = "Three concentric storage tiers step down in diameter from the bottom to the top."


def draw(s):
    for radius, bottom, height in ((34, 0, 14), (26, 14, 14), (17, 28, 14)):
        platter(s, 0, 0, bottom, radius, height)
        s.line([(x, y, bottom + 6) for x, y in oval(0, 0, radius, radius, 27, 59, 14)], EDGE)
        s.line([(x, y, bottom + 6) for x, y in oval(0, 0, radius, radius, 66, 72, 3)], DETAIL)
    s.ellipse(0, 0, 42, 8, 8, DETAIL)
