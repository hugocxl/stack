from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws.editorial_calendar import desk_calendar
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A standing medical calendar marks a follow-up date with a cross and carries a check badge."


def draw(s):
    calendar = desk_calendar(s)
    calendar.frame(56, 38, 17, 15, 1, EDGE)
    medical_cross(calendar, 64.5, 45.5, 6, BOLD)
    badge(s, "check", *calendar.at(106, 34), 17)
