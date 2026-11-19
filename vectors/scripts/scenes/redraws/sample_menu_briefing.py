from geometry import EDGE
from scenes.redraws._w5 import clipboard, course_rows, place_setting, printed_stroke

DESCRIPTION = "A catering clipboard holds a sample menu with a place-setting emblem and three course rows."


def draw(s):
    face = clipboard(s, 58, 62)
    place_setting(s, face, 28, 40, 8.5)
    for z in (27, 18, 9):
        printed_stroke(s, face, [(12, z), (15, z)], EDGE)
    course_rows(s, face, 20, 27, (24, 19, 22))
