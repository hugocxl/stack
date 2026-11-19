from geometry import BOLD, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w4 import dumbbell_mark
from scenes.redraws.editorial_calendar import desk_calendar

DESCRIPTION = "A standing training calendar shows a dumbbell header and a crescent in the selected date cell."


def draw(s):
    calendar = desk_calendar(s)
    dumbbell_mark(calendar, 53, 8, 12)
    calendar.frame(56, 39, 17, 13, 2, EDGE)
    glyph(s, "moon", *calendar.at(64.5, 45.5), 8, BOLD)
