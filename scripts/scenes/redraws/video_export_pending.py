from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import arrow, badge
from scenes.redraws._w4 import paper, play_mark

DESCRIPTION = "A film clapperboard shows an outward export arrow and carries a clock badge."


def draw(s):
    board = paper(s, 73, pitch=.91, run=.32, angle=-25, depth=7)
    board.slab(rounded(0, 0, 104, 73, 3), 7)
    board.line([(0, 19), (104, 19)], EDGE)
    clap = [(0, 0), (93, -26), (98, -13), (3, 12)]
    board.slab(clap, 5)
    for i in range(13, 89, 16):
        v = -i * .28
        board.line([(i, v), (i + 8, v + 10)], EDGE)
    play_mark(board, 28, 46, 13, BOLD)
    arrow(s, [board.at(54, 46), board.at(78, 46)], EDGE, head=7)
    badge(s, "clock", *board.at(103, 49), 17)
