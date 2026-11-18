from geometry import BOLD, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w4 import desktop_display
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A patient portal on a desktop monitor shows a medical cross above two credential fields and a sign-in arrow."


def draw(s):
    display = desktop_display(s, width=96, height=69, angle=9)
    medical_cross(display, 48, 49, 9, BOLD)
    for v in (26, 35):
        display.frame(26, v - 3.5, 44, 7, 2, EDGE)
    display.rows(31, 35, (20,))
    for u in (32, 38, 44, 50):
        display.oval(u, 26, .7, .7, EDGE)
    display.frame(39, 10, 18, 9, 3, EDGE)
    glyph(s, "arrow", *display.at(48, 14.5), 6, EDGE)
