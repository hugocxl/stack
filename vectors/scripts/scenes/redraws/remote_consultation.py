from geometry import BOLD, EDGE
from scenes.redraws._w4 import stethoscope_mark, telehealth_display
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A desktop telehealth call shows a stethoscope and a medical cross in two video tiles."


def draw(s):
    display = telehealth_display(s)
    display.line([(63, 17), (63, 50)], EDGE)
    stethoscope_mark(display, 34, 34, .81, BOLD)
    medical_cross(display, 79, 34, 8, EDGE)
