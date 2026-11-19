from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w2 import pack

DESCRIPTION = "Two identical bound documents overlap with a plus badge at their right corner."


def draw(s):
    for x, y, z in ((17, -10, 0), (0, 13, 16.8)):
        top = pack(s, x, y, z, 72, 69, height=15)
        for v, length in ((29, 34), (39, 45), (49, 29)):
            s.line([(x + 9, y + v, top), (x + 9 + length, y + v, top)], DETAIL)
    badge(s, "plus", 79, 18, 32, 13)
