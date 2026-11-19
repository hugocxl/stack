from geometry import DETAIL
from scenes.redraws._w1 import arc_arrow, file_card

DESCRIPTION = "A curved arrow leads from a front document to an offset backup copy behind it."


def draw(s):
    for x, y in ((-10, -18), (-29, 8)):
        file_card(s, x, y, w=51, h=65)
        for z, length in ((42, 27), (31, 30), (20, 22)):
            s.line([(x + 9, y, z), (x + 9 + length, y, z)], DETAIL)
    arc_arrow(s, (-15, 8, 66), (20, -18, 58), 22)
