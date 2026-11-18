from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow, coin

DESCRIPTION = "A ball follows an arc over a freestanding threshold bar."


def draw(s):
    for x in (-25, 24):
        s.box(x - 5, -6, 0, 10, 13, 5, 3)
        s.box(x - 2, -2, 5, 4, 5, 32, 1.6)
    s.tube([(-26, 0, 35), (26, 0, 35)], 2.4)
    s.line([(-51, 0, 2), (54, 0, 2)], DETAIL, dashed=True)
    path = [(-45, 0, 11), (-36, 0, 34), (-24, 0, 52), (-10, 0, 62),
            (6, 0, 64), (22, 0, 56), (35, 0, 42), (46, 0, 19)]
    arrow(s, path, EDGE, head=8)
    coin(s, 1, 1, 64, 8, depth=3, ink=BOLD)
