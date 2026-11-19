from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A nominee card carries a plus badge as it slips into a ballot box."


def draw(s):
    s.box(0, -4, 0, 79, 49, 34, 3)
    top = Surface(s, (0, 45, 34), rise=(-1, 0), back=(0, 0, -1))
    top.rect(9, 26, 61, 7, 2, EDGE)
    ballot = Surface(s, (12, 17, 33), rise=(-.24, 1), back=(0, -1, -.24))
    ballot.plate(rounded(0, 0, 55, 48, 3), 4)
    ballot.rect(8, 20, 13, 13, 2, EDGE)
    ballot.rules(27, 30, [16], ink=EDGE)
    ballot.rules(27, 22, [12])
    badge(s, "plus", *ballot.point(53, 43), 14)
