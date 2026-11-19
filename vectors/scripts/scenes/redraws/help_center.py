from geometry import BOLD
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open help booklet has short lines of reference text facing a large printed question mark."


def draw(s):
    left, right = open_book(s)
    left.rows(15, 18, (34,), ink=BOLD)
    left.rows(15, 30, (31, 34, 24, 28), step=7)
    right.line([(80, 25), (81, 20), (86, 15), (95, 14), (102, 17),
                (106, 23), (105, 30), (100, 35), (95, 39), (94, 45)], BOLD)
    right.oval(94, 54, 2, 2, BOLD)
