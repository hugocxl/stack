from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import board

DESCRIPTION = "Each row of a cross-validation matrix holds out a different column in a clearly stepped diagonal."


def draw(s):
    p = board(s, 102, 99, run=.53, rise=.75, depth=5, level=True)
    for row in range(4):
        for column in range(4):
            x, z = 10 + column * 21, 12 + row * 20
            holdout = row + column == 3
            s.face([p(u, v) for u, v in rounded(x, z, 16, 15, 2)], BOLD if holdout else DETAIL)
            if holdout:
                s.line([p(x + 4, z + 4), p(x + 12, z + 11)], EDGE)
                s.line([p(x + 7, z + 3), p(x + 13, z + 8)], EDGE)
