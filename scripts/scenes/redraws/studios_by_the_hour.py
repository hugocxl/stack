from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A recording studio cutaway contains acoustic panels and a microphone stand with a clock badge attached to the room."


def draw(s):
    s.box(0, 0, 0, 84, 71, 5, 2)
    s.box(0, 0, 5, 84, 5, 54, 2)
    s.box(0, 5, 5, 5, 66, 54, 2)
    for x in (13, 35, 57):
        s.box(x, 5, 23, 16, 2.5, 24, 2, DETAIL)
    s.box(5, 14, 26, 2.5, 23, 17, 2, DETAIL)
    s.disk(47, 40, 5, 13, 10, 3)
    s.tube([(47, 40, 8), (47, 40, 35)], 1.6)
    s.tube([(47, 40, 36), (47, 39, 48)], 5.5, EDGE)
    for z in (42, 46):
        s.line([(44, 44, z), (50, 44, z)], DETAIL)
    badge(s, "clock", 79, 1, 56, 15)
