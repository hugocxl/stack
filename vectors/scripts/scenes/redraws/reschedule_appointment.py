from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import desk_calendar

DESCRIPTION = "A curved arrow moves a marked appointment across a desk calendar to a later date."


def draw(s):
    calendar = desk_calendar(s, reserved={(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2)})
    calendar.rows(32, 68, (30,), ink=EDGE)
    calendar.frame(25, 28, 12, 12, 1.5, EDGE)
    calendar.frame(59, 28, 12, 12, 1.5, EDGE)
    calendar.oval(31, 34, 2.5, 2.5, EDGE)
    path = oval(48, 39, 17, 12, 162, 19, count=26)
    arrow(s, [calendar.at(u, v) for u, v in path] + [calendar.at(65, 35)], BOLD, head=7)
