from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A pull-down presentation screen shows a chart slide with a boxed caption along its lower edge."


def draw(s):
    face = Surface(s, (0, 0, 0), across=(.94, -.34), back=(-.34, -.94, 0))
    s.tube([face.point(48, 5, 4), face.point(48, 25, 4)], 2)
    for p in ((31, 0, 5), (64, 0, 5), (48, 0, -13)):
        s.tube([face.point(48, 9, 4), face.point(*p)], 1.4)
    face.plate(rounded(0, 22, 96, 59, 1.5), 2)
    s.tube([face.point(-3, 81), face.point(99, 81)], 3.4)
    face.rules(13, 67, [29], ink=EDGE)
    face.rules(13, 55, [30, 22], gap=7)
    face.stroke([(60, 42), (60, 66)], EDGE)
    face.stroke([(60, 42), (83, 42)], EDGE)
    for x, top in ((66, 51), (72, 56), (78, 61)):
        face.stroke([(x, 46), (x, top)], EDGE)
    caption = Surface(s, face.point(0, 0, -2), across=face.across, back=face.back)
    caption.plate(rounded(24, 18, 48, 19, 3), 3)
    caption.rules(32, 30, [32, 23], gap=6, ink=BOLD)
