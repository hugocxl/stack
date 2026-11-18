from geometry import BOLD, EDGE
from scenes.redraws._w4 import landscape, open_book

DESCRIPTION = "An open book shows a landscape illustration with an artist's signature flourish directly beneath it."


def draw(s):
    left, right = open_book(s)
    left.rows(11, 17, (36,), ink=EDGE)
    left.rows(11, 27, (44, 37, 43, 31, 42, 33), step=6)
    landscape(right, 72, 10, 43, 35)
    right.line([(73, 58), (80, 52), (86, 49), (89, 51), (87, 55),
                (82, 60), (79, 60), (86, 55), (94, 54), (93, 57),
                (99, 54), (100, 56), (109, 53)], BOLD)
    right.line([(84, 63), (101, 60), (112, 58)], EDGE)
