from geometry import BOLD, EDGE
from scenes.redraws._w4 import desk_calendar, printed_glyph

DESCRIPTION = "A wire-bound desktop calendar has a check printed in one outlined appointment slot."


def draw(s):
    calendar = desk_calendar(s, reserved={(3, 1)})
    calendar.frame(58, 22, 14, 15, 2, EDGE)
    printed_glyph(calendar, "check", 65, 30, 6.5, BOLD)
