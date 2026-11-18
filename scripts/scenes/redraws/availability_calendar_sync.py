from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import desk_calendar

DESCRIPTION = "A wire-bound booking calendar has a refresh badge beside its row of open dates."


def draw(s):
    calendar = desk_calendar(s)
    calendar.rows(35, 68, (23,), ink=EDGE)
    badge(s, "refresh", *calendar.at(94, 67), 15)
