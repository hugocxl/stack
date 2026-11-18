from geometry import EDGE
from scenes.redraws._w4 import clinic_clipboard, printed_glyph

DESCRIPTION = "A clipboard heads three checked preparation lines with a small house pictogram."


def draw(s):
    board = clinic_clipboard(s)
    board.outline([(25, 29), (36, 20), (47, 29), (44, 29), (44, 39),
                   (28, 39), (28, 29)], EDGE)
    board.line([(34, 39), (34, 33), (38, 33), (38, 39)])
    for v in (49, 64, 79):
        printed_glyph(board, "check", 18, v, 5, EDGE, down=True)
        board.rows(27, v, (30,))
