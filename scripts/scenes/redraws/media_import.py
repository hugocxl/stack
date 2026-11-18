from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import media_frame, paper

DESCRIPTION = "A video thumbnail carries a downward import arrow badge on its top edge."


def draw(s):
    page = paper(s, 64, pitch=.62, angle=-8, depth=6)
    page.slab(rounded(0, 0, 100, 64, 4), 6)
    media_frame(page, 7, 7, 86, 47)
    page.rows(11, 59, (35,), ink=EDGE)
    badge(s, "down", *page.at(80, 1), 17)
