from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import paper

DESCRIPTION = "A product proof panel shows a bottle mockup and carries a check badge at its lower corner."


def draw(s):
    board = paper(s, 88, pitch=.85, run=.40, angle=11, depth=10)
    board.slab(rounded(0, 0, 83, 88, 4), 10)
    board.frame(7, 8, 69, 71, 2, DETAIL)
    board.outline([(23, 67), (22, 40), (26, 33), (35, 29), (35, 18),
                   (49, 18), (49, 29), (58, 33), (62, 40), (61, 67),
                   (56, 72), (28, 72)], EDGE)
    board.line([(36, 24), (48, 24)], DETAIL)
    board.frame(32, 44, 20, 17, 2, EDGE)
    board.rows(36, 52, (12,))
    badge(s, "check", *board.at(81, 77), 17)
