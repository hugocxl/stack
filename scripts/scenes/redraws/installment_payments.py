from geometry import DETAIL
from scenes.redraws._w5 import currency_mark, desk_calendar, rect

DESCRIPTION = "A standing payment calendar repeats the same dollar mark across three spaced due dates."


def draw(s):
    face = desk_calendar(s)
    for row in (5, 17):
        for col in (6, 23, 40):
            rect(s, face, col, row, 15, 11, .7, DETAIL)
    for col in (6, 23, 40):
        rect(s, face, col, 29, 15, 11, .8)
        currency_mark(s, face, col + 7.5, 34.5, 3.8)
