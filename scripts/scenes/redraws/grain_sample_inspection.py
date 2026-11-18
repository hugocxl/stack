from geometry import EDGE
from scenes.redraws._w5 import food_loupe

DESCRIPTION = "A magnifying glass sits above a shallow sample dish holding several grain kernels."


def draw(s):
    s.disk(23, 22, 0, 25, 21, 4)
    s.ellipse(23, 22, 4, 21, 17, EDGE)
    for x, y, flip in ((13, 16, 1), (23, 11, -1), (33, 16, 1),
                       (19, 24, -1), (28, 22, -1), (11, 27, 1),
                       (25, 33, 1), (33, 29, -1)):
        hull = [(-4, 0), (-1, -1.8), (1.5, -1.8), (4, 0),
                (1.5, 1.8), (-1, 1.8)]
        s.face([(x + a, y + b + flip*a*.4, 4.1) for a, b in hull])
    food_loupe(s, 23, 25, 15, 17, handle_y=-.73)
