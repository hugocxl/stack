from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import desk_calendar

DESCRIPTION = "An X badge overlaps the selected date on an appointment desk calendar."


def draw(s):
    calendar = desk_calendar(s, reserved={(4, 0), (4, 1)})
    calendar.rows(33, 68, (27,), ink=EDGE)
    calendar.frame(76, 8, 12, 27, 2, EDGE)
    badge(s, "x", *calendar.at(88, 21), 13.5)
