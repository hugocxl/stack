from geometry import BOLD
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import bed_mark
from scenes.redraws.editorial_calendar import desk_calendar

DESCRIPTION = "A standing calendar has a crescent header and repeats a bed symbol across its evening row."


def draw(s):
    calendar = desk_calendar(s)
    glyph(s, "moon", *calendar.at(53, 8), 9, BOLD)
    for u in (18.5, 41.5, 64.5, 87.5):
        bed_mark(s, lambda x, z: calendar.at(x, 129 - z), u, 64.5, .53, BOLD)
