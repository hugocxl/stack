from geometry import DETAIL, EDGE
from scenes.redraws.editorial_calendar import desk_calendar

DESCRIPTION = "A standing meal-plan calendar schedules meals with plate and cutlery emblems in its date grid."


def draw(s):
    calendar = desk_calendar(s)
    for u, v in ((18.5, 26.5), (64.5, 26.5), (41.5, 45.5),
                 (87.5, 45.5), (64.5, 64.5)):
        calendar.oval(u, v, 5.3, 5.3, EDGE)
        calendar.oval(u, v, 2.9, 2.9, DETAIL)
        for x in (u - 8, u + 8):
            calendar.line([(x, v - 5), (x, v + 5)], EDGE)
        calendar.line([(u - 9.5, v - 5), (u - 9.5, v - 1), (u - 6.5, v - 1),
                       (u - 6.5, v - 5)], DETAIL)
