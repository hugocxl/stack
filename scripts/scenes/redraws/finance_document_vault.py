from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import printed_stroke, rect

DESCRIPTION = "A steel filing cabinet has a partly open drawer showing hanging files and a lock badge on the drawer front."


def draw(s):
    s.box(0, 0, 0, 60, 38, 62, 4)
    shell = lambda x, z: (x, 38, z)
    rect(s, shell, 4, 4, 52, 24, 2, EDGE)
    rect(s, shell, 22, 17, 16, 5, 1, DETAIL)
    rect(s, shell, 4, 32, 52, 26, 2, DETAIL)
    for y, tab in ((41, 10), (48, 23), (55, 35)):
        file_face = lambda x, z: (x, y, z)
        shape = [(7, 33), (53, 33), (53, 48), (tab + 11, 48),
                 (tab + 9, 52), (tab, 52), (tab - 2, 48), (7, 48)]
        s.face([file_face(x, z) for x, z in shape])
    s.face([(56, 37, 31), (56, 62, 31), (56, 62, 48), (56, 37, 48)])
    s.box(4, 60, 31, 52, 6, 18, 2)
    face = lambda x, z: (x, 66, z)
    printed_stroke(s, face, [(18, 42), (18, 39), (32, 39), (32, 42)], DETAIL)
    badge(s, "lock", *face(49, 39), 11)
