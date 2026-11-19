from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A labeled name field carries a check badge aligned with the entered value."


def draw(s):
    entry = Surface(s, (0, 0, 0), rise=(-.43, .90), back=(0, -.90, -.43))
    entry.plate(rounded(0, 0, 107, 51, 6), 12)
    entry.rules(11, 38, [24], ink=EDGE)
    entry.rect(10, 9, 82, 21, 4, EDGE)
    entry.stroke([(16, 21), (21, 25), (31, 25), (31, 14), (21, 14), (16, 18)],
                 EDGE, closed=True)
    entry.oval(21, 19.5, 1.6, 1.6, DETAIL)
    entry.rules(38, 19.5, [32], ink=EDGE)
    badge(s, "check", *entry.point(96, 20, -3), 13)
