from geometry import BOLD, DETAIL
from scenes.redraws._w5 import currency_mark, desk_calendar, printed_stroke, rect

DESCRIPTION = "A ring-bound payout calendar has one bracket spanning the date cells that lead to a currency-marked settlement date."


def draw(s):
    face = desk_calendar(s)
    for x in (16, 26, 36, 46):
        printed_stroke(s, face, [(x, 14), (x, 38)], DETAIL)
    printed_stroke(s, face, [(6, 27), (56, 27)], DETAIL)
    for x in (11, 21, 31, 41, 51):
        printed_stroke(s, face, [(x - 2, 33), (x + 2, 33)], DETAIL)
    rect(s, face, 7, 15, 8, 11, 1, DETAIL)
    currency_mark(s, face, 51, 20.5, 4.6)
    printed_stroke(s, face, [(11, 13), (11, 8), (51, 8), (51, 13)], BOLD)
