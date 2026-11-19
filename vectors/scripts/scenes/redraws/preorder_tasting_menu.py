from geometry import DETAIL, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import course_rows, panel, place_setting, printed_stroke, rect

DESCRIPTION = "A tabletop tasting menu shows a plate above two course lines and carries a clock badge."


def draw(s):
    face = lambda x, z: (x, 9 - .52 * z, z)
    s.box(-2, -3, 0, 55, 16, 5, 1.6)
    panel(s, rounded(0, 4, 51, 55, 2), face, 3)
    rect(s, face, 4, 8, 43, 47, 1.5, DETAIL)
    place_setting(s, face, 22, 40, 9.2)
    printed_stroke(s, face, [(12, 24), (39, 24)], DETAIL)
    course_rows(s, face, 13, 19, (25, 19))
    badge(s, "clock", *face(51, 53), 10.5)
