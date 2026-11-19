from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "An open lab notebook pairs ruled observations with a large drawing of cells in a specimen dish."


def draw(s):
    cover = Surface(s, (0, 69, 4), rise=(-1, .20), back=(0, 0, -1))
    cover.plate(rounded(0, 0, 110, 69, 4), 4)
    left = Surface(s, (2, 68, 8), rise=(-1, .20), back=(0, 0, -1))
    left.plate(rounded(0, 1, 53, 67, 2), 4)
    right = Surface(s, (55, 68, 8), rise=(-1, .20), back=(0, 0, -1))
    right.plate(rounded(0, 1, 52, 67, 2), 4)
    left.rules(8, 57, [26], ink=EDGE)
    left.rules(8, 47, [33, 29, 35, 27, 33], gap=8)
    right.oval(26, 37, 19, 20, BOLD)
    right.oval(26, 38, 15, 15, EDGE)
    for x, v, rx, ry in ((19, 34, 4, 4.8), (30, 43, 5.1, 4.4), (31, 31, 3.7, 3.2)):
        right.oval(x, v, rx, ry, EDGE)
        right.oval(x, v, 1, 1)
    right.rules(11, 10, [26])
