from geometry import EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w1 import clipboard, task_rows

DESCRIPTION = "A clipboard holds an intake form with a heart inside a house pictogram above two applicant fields."


def draw(s):
    clipboard(s)
    s.line([(-11, 0, 25), (-11, 0, 34), (0, 0, 42), (11, 0, 34),
            (11, 0, 25), (-11, 0, 25)], EDGE)
    glyph(s, "heart", 0, 0, 32, 5.2, EDGE)
    task_rows(s, (-17, 16, 22), (-17, 6, 29))
