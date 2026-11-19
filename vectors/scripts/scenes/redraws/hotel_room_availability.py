from geometry import BOLD, DETAIL
from scenes.redraws._w5 import bed_mark, desk_calendar, rect

DESCRIPTION = "A standing hotel calendar shows a bed in its header and one clearly outlined available date."


def draw(s):
    face = desk_calendar(s)
    bed_mark(s, face, 31, 47, .65)
    for z in (15.5, 26.5):
        s.line([face(5, z), face(57, z)], DETAIL)
    for x in (9, 24, 39, 54):
        for z in (10, 21, 32):
            if (x, z) == (39, 21):
                rect(s, face, x - 5, z - 4, 10, 8, 1.3, BOLD)
            s.line([face(x - 2.6, z), face(x + 2.6, z)], DETAIL)
