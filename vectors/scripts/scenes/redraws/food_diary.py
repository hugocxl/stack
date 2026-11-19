from geometry import EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open food journal pairs a printed bowl of food with three dated meal entries."


def draw(s):
    meal, entries = open_book(s)
    meal.oval(33, 37, 21, 10, EDGE)
    meal.line([(12, 37), (17, 50), (24, 55), (42, 55), (49, 50), (54, 37)], EDGE)
    for u in (27, 37):
        meal.line([(u, 29), (u + 2, 25), (u - 1, 20), (u + 1, 15)], EDGE)
    for v, length in ((21, 25), (37, 20), (53, 24)):
        entries.frame(76, v - 2, 6, 6, 1, EDGE)
        entries.rows(88, v, (length, length - 6), step=5)
