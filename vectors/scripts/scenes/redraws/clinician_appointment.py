from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws.editorial_calendar import desk_calendar

DESCRIPTION = "A desk calendar highlights a selected date with a medical cross."


def selected_date(s, column, row):
    """Mark a single appointment in the shared desk calendar grid."""
    page = desk_calendar(s)
    for i in range(4):
        for j in range(3):
            if (i, j) != (column, row):
                page.rows(12 + 23*i, 23 + 19*j, (4,), ink=DETAIL)
    u, v = 18.5 + 23*column, 26.5 + 19*row
    page.frame(u - 9.5, v - 7.8, 19, 15.6, 1, EDGE)
    return page, u, v


def draw(s):
    page, u, v = selected_date(s, 2, 1)
    glyph(s, "plus", *page.at(u, v), 8.5, BOLD)
