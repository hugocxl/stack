from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w2 import level_face

DESCRIPTION = "A check badge caps the approved segment of a graduated rate gauge."


def draw(s):
    def point(x, z):
        return level_face(x, z, 1)

    s.box(-21, -17, 0, 42, 34, 8, 5)
    s.box(-5, -6, 8, 10, 12, 19, 3)
    rim = oval(0, 43, 39, 36, count=64)
    s.face([level_face(x + 1, z + 1, -6) for x, z in rim])
    s.face([point(x, z) for x, z in rim])
    s.line([point(x, z) for x, z in oval(0, 43, 29, 27, -36, 216, 48)], DETAIL)
    s.line([point(x, z) for x, z in oval(0, 43, 25, 23, 216, 45, 40)], BOLD)
    outer = oval(0, 43, 34, 31, 0, 180, 6)
    inner = oval(0, 43, 30, 28, 0, 180, 6)
    for a, b in zip(inner, outer):
        s.line([point(*a), point(*b)], EDGE)
    badge(s, "check", *point(18, 60), 13)
