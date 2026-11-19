from geometry import EDGE, rounded
from scenes.redraws._w4 import standing_card

DESCRIPTION = "A handheld mockup has a rotary control below the dashed outline of its unfinished faceplate."


def draw(s):
    face = standing_card(s, 59, 94, angle=7, lean=.37, depth=13)
    plate = rounded(7, 35, 45, 49, 5)
    face.line(plate + plate[:1], EDGE, dashed=True)
    face.line([(12, 41), (47, 78)], dashed=True)
    face.line([(12, 78), (47, 41)], dashed=True)
    face.oval(29.5, 18, 10, 10, EDGE)
    face.oval(29.5, 18, 6.5, 6.5)
    face.line([(29.5, 18), (33, 22)], EDGE)
    for u in (9, 46):
        face.oval(u + 2, 18, 2, 2, EDGE)
