from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow

DESCRIPTION = "A flow arrow sweeps a pair of leaves downstream through an open concrete drainage channel."


def draw(s):
    s.box(-48, -24, 0, 96, 51, 5, 1.5)
    s.box(-48, -24, 5, 96, 7, 23, 1)
    s.face([(48, -17, 28), (48, -17, 5), (48, -7, 5)], EDGE)
    s.face([(-48, -17, 28), (48, -17, 28), (48, -7, 5), (-48, -7, 5)], EDGE)
    s.box(-48, 18, 4.9, 96, 8, 6, 1)
    for x in (-29, -7, 23):
        s.line([(x, -17, 24), (x + 4, -7.5, 6)], DETAIL)
    for x, y in ((-28, 2), (4, -1)):
        s.face([(x - 5, y + 2, 6), (x - 2, y - 2, 7), (x + 6, y - 3, 6),
                (x + 2, y + 2, 6)], EDGE)
        s.line([(x - 5, y + 2, 6), (x + 2, y - 1, 6.5)], DETAIL)
    s.line([(-43, 6, 5), (-35, 5, 5), (-29, 6, 5)], DETAIL)
    arrow(s, [(-17, 12, 5), (0, 10, 5), (18, 7, 5), (36, 6, 5)], BOLD, head=10)
