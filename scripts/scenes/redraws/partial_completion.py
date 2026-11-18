from geometry import DETAIL, EDGE, rounded
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A three-row clipboard shows two checked items and one dashed unfinished row."


def draw(s):
    board = Surface(s, (8, 0, 2), side=True)
    board.plate(rounded(0, 0, 66, 83, 6), 5)
    board.frame(5, 6, 56, 69, 3)
    clip = Surface(s, (11, 0, 2), side=True)
    clip.plate(rounded(18, 72, 30, 15, 4), 3)
    clip.line([(25, 80), (41, 80)], DETAIL)
    for z in (59, 43, 24):
        frame = rounded(12, z - 5.5, 13, 13, 2)
        board.loop(frame, EDGE, dashed=z == 24)
        board.line([(31, z + 1), (52, z + 1)], EDGE, dashed=z == 24)
    for z in (59, 43):
        board.glyph("check", 18.5, z + 1, 7.5)
