from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import desk_calendar

DESCRIPTION = "An appointment desk calendar has a plus badge anchored to a selected date."


def draw(s):
    calendar = desk_calendar(s, reserved={(4, 0), (4, 1)})
    calendar.rows(33, 68, (27,), ink=EDGE)
    calendar.frame(76, 8, 12, 27, 2, EDGE)
    badge(s, "plus", *calendar.at(89, 21), 13.5)
