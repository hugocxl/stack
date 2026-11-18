from geometry import DETAIL, EDGE
from scenes.redraws._w5 import bank_mark, currency_mark, desk_calendar, printed_stroke

DESCRIPTION = "A ring-bound tax calendar shows a treasury emblem above recurring currency marks in its date grid."


def draw(s):
    face = desk_calendar(s)
    bank_mark(s, face, 31, 47, .61)
    for x in (19, 31, 43):
        printed_stroke(s, face, [(x, 8), (x, 38)], DETAIL)
    printed_stroke(s, face, [(7, 23), (55, 23)], DETAIL)
    for x, z in ((13, 30.5), (37, 30.5), (25, 15.5), (49, 15.5)):
        currency_mark(s, face, x, z, 4.7, ink=EDGE)
