from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import clinic_clipboard, wrench_mark

DESCRIPTION = "A technician work order has a wrench heading and a right-pointing transfer badge on its lower corner."


def draw(s):
    board = clinic_clipboard(s)
    wrench_mark(board, 35, 32, .56)
    for v, width in ((51, 34), (65, 29), (79, 24)):
        board.frame(14, v - 3, 6, 6, 1.2, EDGE)
        board.rows(25, v, (width,))
    badge(s, "arrow", *board.at(71, 79), 13)
