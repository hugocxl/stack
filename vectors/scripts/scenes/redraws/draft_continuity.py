from geometry import EDGE
from scenes.redraws._w2 import caret, draft_notebook, face_arrow, rule

DESCRIPTION = "A resume arrow curls down to the caret at the end of a partially written notebook page."


def draw(s):
    point = draft_notebook(s)
    for z, width in ((70, 55), (59, 48), (48, 57), (37, 34)):
        rule(s, point, 12, z, width, EDGE)
    rule(s, point, 12, 23, 29, EDGE)
    caret(s, point, 46, 23)
    face_arrow(s, point, [(70, 43), (73, 36), (73, 30), (69, 25),
                          (63, 23), (51, 23)], head=7)
