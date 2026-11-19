from geometry import EDGE, rounded
from scenes.redraws._w4 import paper

DESCRIPTION = "Three adjacent storyboard panels show a ball rising, reaching its apex, and returning to the ground."


def draw(s):
    board = paper(s, 66, pitch=.59, angle=-9, depth=4)
    board.slab(rounded(0, 0, 137, 66, 3), 4)
    for u, cx, cy, trail in (
        (7, 22, 33, [(11, 44), (14, 40), (18, 38)]),
        (50, 69, 20, [(54, 30), (57, 25), (61, 22)]),
        (93, 120, 40, [(103, 22), (109, 25), (115, 32)]),
    ):
        board.frame(u, 8, 37, 45, 2, EDGE)
        board.line([(u + 4, 47), (u + 33, 47)])
        board.line(trail, dashed=True)
        board.oval(cx, cy, 5.7, 5.7, EDGE)
        board.rows(u + 2, 60, (21,))
