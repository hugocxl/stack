from geometry import EDGE, oval, rounded
from scenes.redraws._w4 import desk_calendar

DESCRIPTION = "Three dates in a standing appointment calendar contain nameplate symbols for assigned team coverage."


def draw(s):
    calendar = desk_calendar(s, reserved={(0, 2), (1, 2), (2, 1), (3, 0), (4, 0)})
    calendar.rows(26, 68, (17,), ink=EDGE)
    calendar.rows(50, 68, (17,), ink=EDGE)
    slots = ((10, 38, 25, oval(16, 44.5, 2.6, 2.6, count=20)),
             (41, 23, 19, [(47, 27), (50, 29.5), (47, 32), (44, 29.5)]),
             (58, 7, 29, rounded(62, 11, 5, 5, .8)))
    for u, v, width, symbol in slots:
        calendar.frame(u, v, width, 13, 2, EDGE)
        calendar.outline(symbol, EDGE)
        calendar.rows(u + 11, v + 6.5, (width - 15,))
