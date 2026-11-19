from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge, coin
from scenes.redraws._w4 import Surface

DESCRIPTION = "A video camera with a projecting lens and carry handle carries a broadcast-wave badge."


def draw(s):
    s.box(0, 0, 0, 39, 75, 58, 6)
    s.tube([(20, 23, 58), (20, 23, 81), (20, 58, 81), (20, 58, 58)], 4)
    side = Surface(s, lambda u, v: (39, u, v))
    side.frame(8, 14, 52, 29, 3, DETAIL)
    side.rows(15, 24, (21, 12), step=8)
    coin(s, 20, 97, 31, 20, depth=24)
    coin(s, 20, 103, 31, 21, depth=6)
    front = Surface(s, lambda u, v: (u, 103, v))
    front.oval(20, 31, 14, 14, EDGE)
    front.oval(20, 31, 8, 8, DETAIL)
    badge(s, "wifi", 38, 3, 72, 18)
