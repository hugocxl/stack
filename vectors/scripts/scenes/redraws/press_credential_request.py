from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import camera_emblem, paper

DESCRIPTION = "A clipped press credential shows a camera emblem and carries a clock badge at its lower corner."


def draw(s):
    card = paper(s, 88, pitch=.83, run=.62, angle=10, depth=4)
    card.slab(rounded(0, 0, 64, 88, 5), 4)
    card.frame(22, 6, 20, 8, 4, EDGE)
    card.slab(rounded(26, -11, 12, 22, 3), 5)
    card.rows(29, -5, (6,))
    camera_emblem(card, 14, 30, 36)
    card.rows(14, 67, (31, 20), step=8)
    badge(s, "clock", *card.at(65, 68), 15)
