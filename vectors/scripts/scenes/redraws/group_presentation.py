from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "Two standing presenter microphones share one framed presentation board."


def draw(s):
    for x in (5, 69):
        s.box(x, 2, 0, 5, 7, 74, 1)
        s.box(x - 5, -3, 0, 15, 21, 3, 2)
    board = Surface(s, (0, 12, 36))
    board.plate(rounded(0, 0, 79, 53, 3), 5)
    board.rect(5, 5, 69, 43, 1)
    board.rules(13, 37, [28], ink=EDGE)
    board.rules(13, 27, [22, 19], gap=7)
    board.stroke([(43, 15), (51, 22), (58, 18), (67, 32)], BOLD)
    for x, y, z in ((29, 33, 44), (79, 49, 46)):
        s.disk(x, y, 0, 10, 10, 3)
        s.tube([(x, y, 3), (x, y, z), (x - 4, y + 4, z + 6)], 1.3)
        s.tube([(x - 8, y + 6, z + 4), (x - 1, y + 2, z + 8)], 2.6)
