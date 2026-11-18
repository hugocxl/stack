from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import platter

DESCRIPTION = "Two groups of disk platters taper toward a narrow center gap, with arrows pointing inward."


def draw(s):
    for z, radius, height in ((0, 30, 8), (8, 27, 7), (15, 23, 6),
                              (21, 13, 8), (29, 23, 6), (35, 27, 7), (42, 30, 8)):
        platter(s, 0, 0, z, radius, height)

    arrow(s, [(28, -28, 50), (28, -28, 30)], BOLD, head=7)
    arrow(s, [(28, -28, 0), (28, -28, 20)], BOLD, head=7)
