from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import bed_mark, panel

DESCRIPTION = "A standing hotel reservation card shows a bed and a clock set to two o’clock with a check badge at the upper corner."


def draw(s):
    face = lambda x, z: (x, -z*.46, z)
    s.face([(0, -39, 0), (65, -39, 0), face(65, 48), face(0, 48)], DETAIL)
    s.face([(65, -39, 0), (65, 0, 0), face(65, 48)], EDGE)
    panel(s, rounded(0, 0, 65, 48, 3), face, 3.8)
    bed_mark(s, face, 21, 30, .95)
    s.line([face(8, 12), face(31, 12)], DETAIL)
    s.line([face(8, 17), face(27, 17)], DETAIL)
    s.line([face(x, z) for x, z in oval(49, 21, 10.5, 10.5, count=32)], EDGE)
    s.line([face(49, 29), face(49, 21), face(54, 24)], EDGE)
    badge(s, "check", 61, -19, 46, 11)
