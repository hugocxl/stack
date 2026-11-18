from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, microphone

DESCRIPTION = "A team assignment board aligns three removable name strips with pen, magnifier and microphone role symbols."


def draw(s):
    board = Surface(s, (0, 0, 0))
    board.plate(rounded(0, 0, 90, 85, 4), 8)
    board.rules(8, 74, [42], ink=BOLD)
    for v in (54, 34, 14):
        card = Surface(s, (0, 2, 0))
        card.plate(rounded(8, v - 7, 49, 14, 2), 2)
        card.rules(15, v, [34], ink=EDGE)
    pen = board.viewer_axes(70, 54)
    board.stroke([pen(u, v) for u, v in
                  ((-7, -6), (-5, 0), (5, 9), (9, 5), (-1, -4))], EDGE, closed=True)
    board.stroke([pen(-5, 0), pen(-1, -4)])
    board.oval(71, 36, 5.3, 5.3, EDGE)
    board.stroke([(75, 32), (80, 27)], EDGE)
    microphone(board, 73, 12, 12)
