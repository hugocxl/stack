from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import coin
from scenes.redraws._w2 import currency

DESCRIPTION = "A currency coin meets the center of an upright bullseye."


def draw(s):
    s.box(-28, -15, 0, 57, 35, 8, 5)
    s.box(-4, -3, 8, 8, 10, 32, 3)
    y, z = 4, 47
    coin(s, 0, y, z, 32, depth=7)
    for r in (26, 19):
        s.line([(x, y, v) for x, v in oval(0, z, r, r)], DETAIL)
    coin(s, 0, y + 2.5, z, 12, depth=3, ink=EDGE)
    currency(s, lambda x, v: (x, y + 2.5, v), 0, z, .93, BOLD)
