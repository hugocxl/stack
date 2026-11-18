from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws.editorial_calendar import desk_calendar

DESCRIPTION = "A standing calendar shows a curved arrow moving an appointment from one date square to the next."


def draw(s):
    calendar = desk_calendar(s)
    for u in (32, 55):
        calendar.frame(u, 38, 19, 15, 2, EDGE)
    calendar.oval(41.5, 46, 2.5, 2.5, EDGE)
    curve = oval(53, 48, 12, 16, 187, 337, count=32)
    arrow(s, [calendar.at(u, v) for u, v in curve], BOLD, head=6)
