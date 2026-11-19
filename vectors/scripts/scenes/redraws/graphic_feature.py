from geometry import EDGE
from scenes.redraws._w4 import closed_book

DESCRIPTION = "An illustrated feature cover shows a lighthouse and waves above a short headline."


def draw(s):
    cover = closed_book(s, angle=-11, width=83, height=101, depth=9)
    cover.frame(14, 10, 60, 57, 3, EDGE)
    cover.oval(59, 24, 5, 5)
    cover.outline([(33, 51), (36, 31), (45, 31), (48, 51)], EDGE)
    cover.outline([(34, 31), (34, 27), (40.5, 21), (47, 27), (47, 31)], EDGE)
    cover.line([(35, 41), (46, 41)], EDGE)
    for v in (51, 58):
        cover.line([(15, v), (25, v - 2), (34, v), (44, v + 2), (53, v), (63, v - 2),
                    (73, v)])
    cover.rows(15, 77, (47,), ink=EDGE)
    cover.rows(15, 85, (35, 27), step=6)
