from geometry import BOLD, EDGE
from scenes.redraws._w3 import desk_calendar, printed_check

DESCRIPTION = "A desk calendar marks four consecutive study days with checks in one continuous band."


def draw(s):
    face = desk_calendar(s, 96, 79)
    face.rules(33, 62, [30], ink=EDGE)
    face.rect(10, 12, 76, 33, 3)
    face.stroke([(10, 26), (86, 26)])
    for x in (29, 48, 67):
        face.stroke([(x, 12), (x, 45)])
    face.rect(10, 26, 76, 19, 3, BOLD)
    for x in (19.5, 38.5, 57.5, 76.5):
        printed_check(face, x, 35, 7)
    for x in (19.5, 38.5, 57.5, 76.5):
        face.oval(x, 19, 1.6, 1.6)
