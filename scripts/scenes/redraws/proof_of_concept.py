from geometry import EDGE, rounded
from scenes.redraws._w4 import Surface

DESCRIPTION = "A thick prototype screen holds a dashed wireframe with a picture block and two empty controls."


def draw(s):
    s.box(0, 0, 0, 81, 14, 68, 5)
    face = Surface(s, lambda u, v: (u, 14, v))
    face.frame(6, 6, 69, 55, 3, EDGE)
    face.line([(6, 50), (75, 50)], EDGE)
    for u, v, width, height in ((13, 13, 31, 30), (51, 30, 17, 13), (51, 13, 17, 10)):
        outline = rounded(u, v, width, height, 2)
        face.line(outline + outline[:1], EDGE, dashed=True)
    face.line([(16, 16), (41, 40)], EDGE, dashed=True)
    face.line([(16, 40), (41, 16)], EDGE, dashed=True)
