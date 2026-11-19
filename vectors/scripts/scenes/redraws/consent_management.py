from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import rect

DESCRIPTION = "A desktop preferences screen shows three category rows with separate switches in on and off positions."


def draw(s):
    s.box(20, -11, 0, 26, 21, 4, 5)
    s.box(29, -7, 4, 8, 5, 20, 1)
    s.box(0, -7, 19, 66, 10, 47, 3.5)
    face = lambda x, z: (x, 3, z)
    rect(s, face, 4, 23, 58, 39, 2, DETAIL)
    for z, width, knob in ((32, 13, 42), (43, 18, 52), (54, 15, 52)):
        s.line([face(11, z), face(11 + width, z)], EDGE)
        rect(s, face, 37, z - 3.8, 20, 7.6, 3.8, EDGE)
        s.line([face(x, h) for x, h in oval(knob, z, 2.4, 2.4, count=24)], EDGE)
