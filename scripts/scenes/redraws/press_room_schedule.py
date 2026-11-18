from geometry import EDGE
from scenes.redraws._w4 import Surface
from scenes.redraws._w5 import desk_calendar

DESCRIPTION = "A tent calendar shows a lectern pictogram above its date grid."


def draw(s):
    at = desk_calendar(s)
    calendar = Surface(s, at)
    calendar.outline([(21, 35), (40, 35), (37, 30), (24, 30)], EDGE)
    calendar.outline([(27, 30), (34, 30), (34, 23), (27, 23)], EDGE)
    calendar.line([(23, 23), (38, 23)], EDGE)
    calendar.line([(30, 35), (30, 37), (35, 39)], EDGE)
    for z in (5, 12, 19):
        calendar.line([(7, z), (55, z)])
    for u in (7, 19, 31, 43, 55):
        calendar.line([(u, 5), (u, 19)])
    calendar.frame(32.7, 12.8, 8.7, 5.2, .6, EDGE)
