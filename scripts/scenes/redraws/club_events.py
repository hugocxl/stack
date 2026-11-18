from geometry import EDGE
from scenes.redraws._w3 import desk_calendar, printed_glyph

DESCRIPTION = "A ring-bound desk calendar marks one upcoming date with a star."


def draw(s):
    face = desk_calendar(s, w=88, h=75)
    face.rules(15, 57, [30], ink=EDGE)
    for row, v in enumerate((13, 29)):
        for column, x in enumerate((12, 29, 46, 63)):
            if (row, column) == (0, 2):
                printed_glyph(face, "star", x + 6.5, v + 5, 10)
            else:
                face.rect(x, v, 13, 10, 1, EDGE)
