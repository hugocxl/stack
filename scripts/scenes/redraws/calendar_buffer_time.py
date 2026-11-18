from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import desk_calendar, printed_glyph

DESCRIPTION = "A wire-bound schedule shows a bold bracket spanning the gap between two appointments."


def draw(s):
    calendar = desk_calendar(s, reserved={(column, row) for column in range(5) for row in range(3)})
    calendar.line([(7, 30), (87, 30)], DETAIL)
    for x in (7, 62):
        calendar.frame(x, 23, 25, 14, 3, EDGE)
        printed_glyph(calendar, "clock", x + 7, 30, 4, DETAIL)
        calendar.rows(x + 14, 30, (6,))
    calendar.line([(32, 18), (32, 12), (62, 12), (62, 18)], BOLD)
    for x in (32, 62):
        calendar.line([(x, 18), (x, 23)], DETAIL)
