from geometry import BOLD, EDGE
from scenes.redraws._w3 import clipboard, printed_glyph, question

DESCRIPTION = "A rule on a clipboard branches from one decision diamond to two action boxes."


def draw(s):
    board = clipboard(s, 93, 102)
    board.stroke([(46, 79), (67, 63), (46, 47), (25, 63)], BOLD, closed=True)
    question(board, 46, 64, 14, EDGE)
    board.stroke([(26, 63), (21, 63), (21, 35)], EDGE)
    board.stroke([(66, 63), (72, 63), (72, 35)], EDGE)
    for x, kind in ((21, "check"), (72, "x")):
        printed_glyph(board, "down", x, 30, 7, EDGE)
        board.rect(x - 13, 9, 26, 16, 3, EDGE)
        printed_glyph(board, kind, x, 17, 8)
