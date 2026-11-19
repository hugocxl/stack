from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow

DESCRIPTION = "A data table transforms uneven entries into aligned decimal columns."


def draw(s):
    s.box(0, -15, 0, 104, 15, 87, 4)
    def p(x, z):
        return x, 0, z

    for z in (12, 29, 60, 77):
        s.line([p(10, z), p(94, z)], DETAIL)
    for x in (38, 66):
        s.line([p(x, 83), p(x, 53)], DETAIL)
        s.line([p(x, 33), p(x, 8)], DETAIL)
    lengths = ((14, 8, 18), (7, 15, 11))
    for row, z in enumerate((68, 80)):
        for column, x in enumerate((16, 43, 70)):
            dx = (row + column * 3) % 5
            s.line([p(x + dx, z), p(x + dx + lengths[row][column], z)], EDGE)
    for z in (17, 25):
        for x in (16, 44, 72):
            s.line([p(x, z), p(x + 5, z)], EDGE)
            s.line([p(x + 8, z), p(x + 8.8, z)], BOLD)
            s.line([p(x + 12, z), p(x + 17, z)], EDGE)
    arrow(s, [p(53, 52), p(53, 37)], BOLD, head=6)
