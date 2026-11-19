from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import flat

DESCRIPTION = "A tabbed portfolio folio holds a work sample and carries an upload badge."


def draw(s):
    bottom = flat(s, 0, 76, 4)
    bottom.plate([(0, 0), (96, 0), (96, 68), (48, 68),
                  (43, 76), (6, 76), (0, 70)], 4)
    papers = flat(s, 0, 76, 10)
    papers.plate(rounded(7, 6, 78, 64, 2), 6)
    papers.rect(18, 49, 27, 16, 2, EDGE)
    papers.stroke([(21, 51), (28, 59), (33, 55), (37, 61), (42, 54)])
    papers.rules(52, 60, [24, 16], gap=5)
    cover = flat(s, 0, 76, 13)
    cover.plate([(0, 0), (96, 0), (96, 45), (59, 45), (54, 40),
                 (38, 40), (33, 45), (0, 45)], 4)
    cover.stroke([(9, 7), (9, 38)])
    cover.rect(40, 12, 27, 9, 2)
    badge(s, "up", *cover.point(92, 8), 14)
