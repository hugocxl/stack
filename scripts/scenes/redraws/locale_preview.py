from geometry import EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "An angled web preview shows a globe in its header above a rendered headline and short paragraph."


def draw(s):
    s.box(29, -21, 0, 45, 35, 5, 6)
    s.box(46, -10, 5, 11, 8, 21, 2)
    face = Surface(s, (0, 0, 19), rise=(-.17, .98), back=(0, -.98, -.17),
                   across=(.99, -.12))
    face.plate(rounded(0, 0, 105, 69, 5), 8)
    face.rect(5, 6, 95, 57, 3, EDGE)
    face.stroke([(5, 45), (100, 45)], EDGE)
    globe = face.viewer_axes(19, 54)
    for rx in (3, 6):
        face.stroke([globe(x, v) for x, v in oval(0, 0, rx, 6)], EDGE)
    face.stroke([globe(-6, 0), globe(6, 0)], EDGE)
    face.rules(35, 54, [28], ink=EDGE)
    face.rules(14, 35, [48], ink=EDGE)
    face.rules(14, 24, [72, 53, 43], gap=6)
