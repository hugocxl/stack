from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "A security code slip shows three rows of grouped code blocks and carries a lock badge."


def draw(s):
    face = lambda x, z: (x, -.48 * z, z)
    panel(s, rounded(0, 0, 50, 67, 3), face, 3)
    s.line([face(6, 53), face(44, 53)], DETAIL, dashed=True)
    for z in (15, 28, 41):
        for start in (8, 28):
            for x in (start, start + 5, start + 10):
                rect(s, face, x, z - 2, 2.8, 4, .25, EDGE)
    badge(s, "lock", *face(47, 61), 13)
