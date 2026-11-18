from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow

DESCRIPTION = "Every third parcel rises above a line of evenly spaced parcels on a roller conveyor."


def draw(s):
    for x in (4, 75):
        s.box(x, 0, 0, 7, 22, 12, 2)
    s.box(0, 0, 12, 86, 24, 8, 3)
    for x in range(5, 85, 6):
        s.line([(x, 3, 20), (x, 21, 20)], DETAIL)
    for i in range(6):
        x = 4 + i * 13.5
        if (i + 1) % 3 == 0:
            arrow(s, [(x + 5, 12, 23), (x + 5, 12, 40)], EDGE, head=5)
            s.box(x, 6, 45, 10, 13, 9, 1.4, BOLD)
        else:
            s.box(x, 6, 20, 10, 13, 9, 1.4)
    arrow(s, [(27, 24, 16), (61, 24, 16)], EDGE, head=5)
