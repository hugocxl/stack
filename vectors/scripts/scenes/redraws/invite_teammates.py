from scenes.redraws._kit import badge, coin
from scenes.redraws._w1 import portrait_mark

DESCRIPTION = "Three overlapping teammate portrait tokens carry one plus badge."


def draw(s):
    for x, y, z, r in ((-25, -4, 26, 15), (26, -4, 27, 15), (0, 3, 24, 19)):
        coin(s, x, y, z, r, depth=5)
        portrait_mark(s, x, y, z, .86 * r, ring=False)
    badge(s, "plus", 29, 2, 15, 11.5)
