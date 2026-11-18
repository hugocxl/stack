from geometry import EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w4 import capsule_mark, standing_card, stethoscope_mark
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A clinic team roster shows three credential tiles marked with a stethoscope, a capsule, and a heart."


def draw(s):
    board = standing_card(s, 110, 73, angle=-20, lean=.25, depth=7)
    medical_cross(board, 15, 59, 6, EDGE)
    board.rows(28, 59, (42,), ink=EDGE)
    board.line([(8, 47), (102, 47)])
    for u in (22, 55, 88):
        board.frame(u - 12, 12, 24, 32, 2, EDGE)
        board.frame(u - 3, 40, 6, 1.4, .6)
        board.rows(u - 7, 16, (14,))
    stethoscope_mark(board, 21, 28, .50)
    capsule_mark(board, 55, 28, 8)
    glyph(s, "heart", *board.at(88, 28), 10, EDGE)
