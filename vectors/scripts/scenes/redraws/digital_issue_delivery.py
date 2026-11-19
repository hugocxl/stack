from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import landscape, paper

DESCRIPTION = "A tablet displays a magazine cover with a download badge at its lower corner."


def draw(s):
    tablet = paper(s, 101, pitch=.85, run=.43, angle=-22, depth=8)
    tablet.slab(rounded(0, 0, 74, 101, 6), 8)
    tablet.frame(6, 7, 62, 84, 3, EDGE)
    tablet.rows(13, 18, (46,), ink=BOLD)
    landscape(tablet, 13, 31, 48, 34)
    tablet.rows(13, 73, (32, 24), step=6)
    tablet.rows(29, 96, (16,), ink=EDGE)
    badge(s, "down", *tablet.at(76, 80), 13)
