from geometry import EDGE, rounded
from scenes.redraws._w4 import desk_calendar

DESCRIPTION = "A wire-bound appointment calendar marks a group booking with three seats in the selected date block."


def draw(s):
    reserved = {(column, row) for column in (2, 3, 4) for row in (1, 2)}
    calendar = desk_calendar(s, reserved=reserved)
    calendar.rows(30, 68, (34,), ink=EDGE)
    calendar.frame(42, 24, 46, 27, 2, EDGE)
    for x in (48, 61, 74):
        calendar.outline(rounded(x + 1, 35, 8, 10, 2), EDGE)
        calendar.outline(rounded(x, 31, 10, 5, 1.5), EDGE)
        calendar.line([(x + 5, 31), (x + 5, 28)], EDGE)
