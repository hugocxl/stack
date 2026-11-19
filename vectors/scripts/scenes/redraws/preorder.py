from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "An open shopping bag with loop handles carries a prominent clock badge."


def draw(s):
    def handle(y):
        s.tube([(-12, y, 43), (-12, y, 53), (-8, y, 59), (0, y, 61),
                (8, y, 59), (12, y, 53), (12, y, 43)], 1.4, EDGE)

    s.face([(-27, -14, 0), (27, -14, 0), (29, -17, 43), (-29, -17, 43)], EDGE)
    s.face([(-27, -14, 0), (-27, 14, 0), (-29, 17, 43), (-29, -17, 43)], DETAIL)
    handle(-16.8)

    s.face([(27, -14, 0), (27, 14, 0), (29, 17, 43), (29, -17, 43)], EDGE)
    s.line([(29, 0, 43), (27, 0, 8), (27, 13, 1)], DETAIL)
    s.face([(-27, 14, 0), (27, 14, 0), (29, 17, 43), (-29, 17, 43)], EDGE)
    handle(16.8)
    badge(s, "clock", 31, 19, 36, 13)
