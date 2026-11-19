from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow

DESCRIPTION = "A bold route arrow turns into the aisle between two rows of warehouse shelving."


def draw(s):
    s.box(-44, -31, 0, 88, 67, 3, 2)
    s.box(-44, -31, 3, 88, 3, 9, 1)

    def row(x):
        s.box(x, -24, 3, 17, 43, 4, 1)
        for y in (-21, -7, 7):
            s.box(x + 2, y, 7, 13, 10, 9, 1)
            s.line([(x + 8, y, 16), (x + 8, y + 10, 16)], DETAIL)
        for end in (-23, 18):
            s.line([(x, end, 7), (x, end, 20), (x + 17, end, 20),
                    (x + 17, end, 7)], EDGE)
        s.line([(x, -23, 20), (x, 18, 20)], EDGE)

    row(-38)
    row(23)
    arrow(s, [(27, 28, 3), (-2, 28, 3), (-6, 24, 3), (-6, -22, 3)], BOLD, head=9)
