from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface
from scenes.redraws._w5 import clipboard
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A patient intake clipboard with a medical cross and three short form fields carries a check badge."


def draw(s):
    page = Surface(s, clipboard(s, 65, 89))
    medical_cross(page, 32.5, 62, 11, BOLD)
    for v in (21, 32, 43):
        page.frame(12, v - 2, 6, 4, 1, EDGE)
        page.rows(24, v, (27,))
    badge(s, "check", *page.at(65, 27), 16)
