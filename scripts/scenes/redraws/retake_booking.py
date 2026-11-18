from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import desk_calendar

DESCRIPTION = "A ring-bound exam appointment calendar pairs a date block with a refresh badge."


def draw(s):
    face = desk_calendar(s, 85, 79)
    face.rules(26, 61, [33], ink=EDGE)
    face.rect(10, 12, 32, 30, 2, EDGE)
    face.stroke([(10, 34), (42, 34)], EDGE)
    for x in (18, 26, 34):
        for v in (20, 27):
            face.oval(x, v, 1.35, 1.35, EDGE)
    for v in (25, 17):
        face.rules(49, v, [8])
        for x in (64, 72):
            face.oval(x, v, 2.1, 2.1, EDGE)
    badge(s, "refresh", *face.point(82, 39), 14)
