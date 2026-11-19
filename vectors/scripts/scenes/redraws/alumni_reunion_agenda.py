from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, cover_cap

DESCRIPTION = "A looped reunion lanyard holds a large alumni pass with a mortarboard and three agenda entries."


def draw(s):
    s.tube([(37, 5, 77), (22, 6, 96), (16, 17, 111), (19, 33, 120),
            (31, 40, 119), (47, 43, 111), (50, 37, 101), (46, 24, 92),
            (38, 5, 77)], 2.5)
    face = Surface(s, (0, 6, 0), rise=(-.08, 1), back=(0, -1, -.08))
    face.plate(rounded(0, 0, 74, 80, 6), 6)
    face.rect(28, 69, 18, 5, 2, EDGE)
    cover_cap(face, 37, 52, 35)
    for v, length in ((28, 34), (19, 39), (10, 29)):
        face.rect(13, v - 2, 4, 4, 1, EDGE)
        face.rules(24, v, [length], ink=EDGE)
