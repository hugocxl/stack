from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, open_book
from scenes.redraws.hydration_history import date_mark

DESCRIPTION = "An open recovery journal pairs a dated bandage entry with a stepped soreness scale."


def draw(s):
    left, right = open_book(s)
    date_mark(left, 12, 12, 1.15)
    left.rows(29, 13, (22,))
    bandage = Surface(s, lambda u, v: left.at(34 + .78*u + .62*v, 44 - .62*u + .78*v))
    bandage.outline(rounded(-21, -8, 42, 16, 7), BOLD)
    bandage.frame(-7, -7.9, 14, 15.8, 1, EDGE)
    for u in (-13, 13):
        bandage.oval(u, -3, 1.2, 1.2)
        bandage.oval(u, 3, 1.2, 1.2)
    right.rows(74, 13, (28, 20), step=6, ink=DETAIL)
    right.line([(73, 50), (110, 50)], DETAIL)
    for u, height in ((73, 6), (82, 10), (91, 14), (100, 18), (109, 22)):
        right.frame(u, 50 - height, 4.5, height, .7, EDGE)
    right.oval(93.25, 32, 2.1, 2.1, BOLD)
    right.rows(74, 60, (31,), ink=DETAIL)
