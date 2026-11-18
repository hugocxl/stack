from geometry import BOLD
from scenes.redraws._kit import badge
from scenes.redraws._w4 import stethoscope_mark, telehealth_display

DESCRIPTION = "A desktop telehealth call shows a stethoscope in its video area and carries a clock badge."


def draw(s):
    display = telehealth_display(s)
    stethoscope_mark(display, 45, 34, .83, BOLD)
    badge(s, "clock", *display.at(95, 48), 18)
