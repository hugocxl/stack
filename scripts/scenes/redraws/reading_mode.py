from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A compact reader window gives one centered text column broad blank margins."


def draw(s):
    s.box(27, -24, 0, 58, 31, 5, 5)
    s.box(43, -14, 4, 26, 9, 12, 3)
    screen = Surface(s, (0, 0, 12), rise=(-.13, .99), back=(0, -.99, -.13))
    screen.plate(rounded(0, 0, 112, 72, 6), 8)
    screen.rect(5, 7, 102, 59, 3, EDGE)
    screen.rules(35, 53, [36], ink=EDGE)
    screen.rules(35, 43, [43, 41, 39, 43, 29], gap=6, ink=EDGE)
