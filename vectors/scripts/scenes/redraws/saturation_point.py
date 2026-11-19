from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w2 import level_face

DESCRIPTION = "A laboratory thermometer reaches the end of its graduated scale."


def draw(s):
    s.box(-21, -17, 0, 42, 34, 7, 4)
    def point(x, z):
        return level_face(x, z, 1)

    bulb = oval(0, 21, 14, 14, 120, 420, 44)
    cap = oval(0, 81, 7, 7, 0, 180, 20)
    shape = [*bulb, *cap]
    s.face([level_face(x + 3, z + 2, -3) for x, z in shape])
    s.face([point(x, z) for x, z in shape])
    s.tube([point(0, 21), point(0, 80)], 2.8, BOLD)
    for z in (37, 48, 59, 70, 81):
        s.line([point(12, z), point(28 if z == 81 else 22, z)],
               EDGE if z == 81 else DETAIL)
