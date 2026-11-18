from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import clinic_clipboard, printed_glyph

DESCRIPTION = "A partially completed booking checklist on a clipboard has a curved arrow returning to its first unfilled field."


def draw(s):
    board = clinic_clipboard(s)
    board.frame(12, 23, 17, 16, 2, EDGE)
    board.line([(12, 29), (29, 29)], EDGE)
    for u in (16, 25):
        board.line([(u, 21), (u, 26)], EDGE)
    board.rows(36, 29, (23, 17), step=7)
    for v in (49, 63, 77):
        board.frame(13, v - 3, 7, 7, 1)
        board.rows(26, v + 1, (21 if v == 49 else 15,))
    printed_glyph(board, "check", 16.5, 49, 5, EDGE, down=True)
    curve = oval(59, 66, 15, 13, 89, -143, count=32)
    arrow(s, [board.at(u, v) for u, v in curve], BOLD, head=7)
