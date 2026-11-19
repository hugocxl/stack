from geometry import DETAIL, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import mountain_mark, panel, rect

DESCRIPTION = "A clipped park permit displays a mountain pictogram and carries an approval check badge."


def draw(s):
    board = lambda x, z: (x, 4 - .32*z, z)
    face = lambda x, z: (x, 5.5 - .32*z, z)
    panel(s, rounded(0, 0, 46, 58, 3.6), board, 6)
    panel(s, rounded(4, 4, 38, 49, 1.3), face, 1, DETAIL)
    s.tube([board(13, 53), board(13, 59), board(32, 59), board(32, 53)], 1.5)
    rect(s, face, 8, 25, 30, 21, 1.1, DETAIL)
    mountain_mark(s, face, 23, 34, .77)
    for z, length in ((19, 24), (13, 19)):
        s.line([face(9, z), face(9 + length, z)], DETAIL)
    badge(s, "check", 46, -3, 33, 12)
