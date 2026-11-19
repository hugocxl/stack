from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface

DESCRIPTION = "A treadmill with a running belt, paired handrails and a raised console carries a history clock badge."


def draw(s):
    s.box(-52, -26, 0, 113, 52, 8, 6)
    belt = Surface(s, lambda u, v: (u, v, 8))
    belt.frame(-45, -17, 98, 34, 4, EDGE)
    for u in (41, 47):
        belt.line([(u, -15), (u, 15)], DETAIL)
    for y in (-22, 22):
        s.tube([(-48, y, 7), (-53, y, 42), (-48, y, 57), (-32, y, 58),
                (-15, y, 53)], 2.8, EDGE)

    console = Surface(s, lambda u, v: (-52 + v*.72, -u, 64 - v*.57))
    console.slab(rounded(-26, 0, 52, 21, 4), 5)
    console.frame(-17, 4, 34, 9, 2, EDGE)
    for u in (-13, 0, 13):
        console.line([(u - 2, 16), (u + 2, 16)], DETAIL)
    badge(s, "clock", -40, -30, 73, 16)
