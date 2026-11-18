from geometry import BOLD, EDGE
from scenes.redraws._w3 import book, cover_cap, flat

DESCRIPTION = "A single notched ribbon hangs from the pages of a closed lesson book."


def draw(s):
    cover = book(s, w=69, h=68, depth=14)
    cover_cap(cover, 39, 44, 35)
    cover.rules(22, 24, [32], ink=EDGE)
    ribbon = flat(s, 0, 70, 8)
    rib = [ribbon.point(x, v) for x, v in ((40, 3), (50, 3), (52, -20), (46, -14), (41, -20))]
    s.face(rib, BOLD)
    s.line([ribbon.point(45, 2), ribbon.point(46, -12)])
