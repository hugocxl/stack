from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "A transcript stands inside an open archive box with speaker marks and timing columns visible above the rim."


def draw(s):
    s.box(0, 0, 0, 65, 35, 6, 2)
    s.face([(0, 0, 5), (65, 0, 5), (65, 0, 29), (0, 0, 29)])
    s.face([(0, 0, 5), (0, 35, 5), (0, 35, 24), (0, 0, 29)], DETAIL)
    face = lambda x, z: (x, 24 - .33 * (z - 7), z)
    panel(s, rounded(7, 7, 50, 65, 2), face, 3)
    s.line([face(14, 63), face(36, 63)], EDGE)
    for z, length in ((51, 21), (40, 18), (29, 22)):
        bubble = [(14, z - 2.5), (14, z + 3.3), (22, z + 3.3), (22, z - 1),
                  (18, z - 1), (15.5, z - 3.5), (15.5, z - 1), (14, z - 1)]
        s.line([face(x, h) for x, h in bubble], EDGE)
        s.line([face(27, z), face(27 + length, z)], EDGE)
        for x in (27, 32):
            s.line([face(x, z - 3), face(x + 2, z - 3)], DETAIL)
    s.face([(65, 0, 5), (65, 35, 5), (65, 35, 24), (65, 0, 29)])
    s.face([(0, 35, 5), (65, 35, 5), (65, 35, 24), (0, 35, 24)])
    rect(s, lambda x, z: (x, 35, z), 23, 15, 19, 4, 2, EDGE)
