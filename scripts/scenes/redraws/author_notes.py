from geometry import BOLD, EDGE
from scenes.redraws._w4 import Surface, open_book

DESCRIPTION = "An open manuscript has one lined note attached to the margin of its right page."


def draw(s):
    left, right = open_book(s)
    left.rows(12, 12, (33,), ink=EDGE)
    left.rows(12, 21, (39, 34, 40, 28, 40, 36, 31), step=6)
    right.rows(71, 13, (35, 31), step=6)
    right.rows(71, 27, (9, 10, 8, 10, 8), step=6)
    right.rows(71, 62, (36,))
    note = Surface(s, lambda u, v: (u, v, right.at(min(u, 120), v)[2] + 2.5))
    note.slab([(85, 24), (126, 24), (126, 50), (117, 59), (85, 59)], 2, EDGE)
    note.line([(117, 59), (117, 50), (126, 50)], EDGE)
    note.rows(91, 33, (27,), ink=BOLD)
    note.rows(91, 41, (28, 20, 16), step=6)
