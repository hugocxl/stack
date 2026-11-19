from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "A workspace window has a persistent navigation sidebar and a closed lock badge on its top corner."


def draw(s):
    face = lambda x, z: (x - z * .32, -x * .37, z)
    panel(s, rounded(0, 0, 71, 52, 4), face, 6)
    s.line([face(1, 42), face(70, 42)], EDGE)
    s.line([face(21, 5), face(21, 42)], EDGE)
    for x in (6, 11, 16):
        s.line([face(x, 47), face(x + 1, 47)], EDGE)
    for z in (14, 22, 30):
        s.line([face(6, z), face(15, z)], DETAIL)
    rect(s, face, 28, 26, 35, 9, 1, DETAIL)
    for x in (28, 47):
        rect(s, face, x, 9, 16, 12, 1, EDGE)
    badge(s, "lock", *face(67, 48), 13)
