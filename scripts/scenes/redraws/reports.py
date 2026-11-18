from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import paper

DESCRIPTION = "A stack of report pages carries a four-bar chart entirely on the top sheet."


def draw(s):
    for level in range(3):
        top = paper(s, 2 * level, -4.5 * level, 1.8 * level, 78, 87, fold=10)
    s.line([(17, 7, top), (48, 7, top)], EDGE)
    s.line([(17, 15, top), (38, 15, top)], DETAIL)
    s.line([(17, 27, top), (17, 66, top), (73, 66, top)], EDGE)
    for x, length in ((23, 12), (36, 21), (49, 17), (62, 33)):
        s.line([(x, 66, top), (x, 66 - length, top), (x + 8, 66 - length, top),
                (x + 8, 66, top)], BOLD)
