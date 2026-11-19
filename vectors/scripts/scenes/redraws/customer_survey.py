from geometry import DETAIL, EDGE
from scenes.redraws._w4 import clinic_clipboard, printed_glyph

DESCRIPTION = "A standing clipboard has a row of rating stars and a pencil clipped along its edge."


def draw(s):
    board = clinic_clipboard(s)
    board.rows(14, 27, (39,), ink=EDGE)
    for u in (17, 29, 41, 53):
        printed_glyph(board, "star", u, 43, 6.5, EDGE)
    for v, width in ((63, 30), (77, 23)):
        board.frame(14, v - 3, 6, 6, 1)
        board.rows(25, v, (width,), ink=DETAIL)
    board.slab([(62, 23), (69, 23), (69, 74), (65.5, 83), (62, 74)], 3)
    board.line([(62, 31), (69, 31)], DETAIL)
    board.line([(62, 74), (69, 74)], DETAIL)
