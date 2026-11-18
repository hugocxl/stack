from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A tripod projection screen shows a presentation slide with a title and three rising bars."


def draw(s):
    for x, y in ((61, 10), (23, 27), (89, 21)):
        s.tube([(x, y, 1.8), (51, 4, 30)], 1.8)
    s.tube([(51, 4, 20), (51, 4, 103)], 2.4)
    screen = Surface(s, (0, 10, 36))
    screen.plate(rounded(0, 0, 102, 62, 2), 3)
    screen.rules(11, 50, [35], ink=EDGE)
    screen.rules(11, 37, [25, 21, 28], gap=7)
    for index, height in enumerate((10, 21, 33)):
        screen.rect(53 + index * 13, 11, 8, height, 1, EDGE)
    screen.rules(50, 11, [40], ink=EDGE)
    s.tube([(-2, 10, 98), (104, 10, 98)], 3.3)
    s.tube([(0, 10, 36), (102, 10, 36)], 1.6)
