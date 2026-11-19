from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import outline

DESCRIPTION = "A written response feeds into a two-bin sorter marked with distinct category tags."


def draw(s):
    s.box(0, 0, 0, 91, 44, 28, 3)
    for x, style in ((10, "round"), (53, "cornered")):
        s.solid([(x, 5), (x + 28, 5), (x + 28, 37), (x, 37)], 27, 1, ink=DETAIL)
        s.line([(x + 3, 8, 28), (x + 3, 34, 28), (x + 25, 34, 28)], EDGE)
        outline(s, x + 4, 44, 6, 21, 14, 2, DETAIL)
        if style == "round":
            s.line([(u, 44, v) for u, v in oval(x + 14, 13, 4.6, 4.6)], EDGE)
        else:
            s.line([(x + 9, 44, 9), (x + 19, 44, 9), (x + 14, 44, 18),
                    (x + 9, 44, 9)], EDGE)
    s.face([(7, 12, 40), (31, 12, 40), (31, 6, 71), (7, 6, 71)])
    for z, length in ((64, 14), (57, 12), (50, 14)):
        y = 12 - (z - 40) * 6/31
        s.line([(12, y, z), (12 + length, y, z)], DETAIL)
    arrow(s, [(20, 24, 48), (23, 24, 32)], BOLD, head=6)
