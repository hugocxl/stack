from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "Text in a recessed field crosses its original right edge into an outlined overflow area."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.55, .84), back=(0, -.84, -.55))
    face.plate(rounded(0, 0, 110, 63, 5), 8)
    world = face.viewer_axes(18, 51)
    for r in (2.5, 5):
        face.stroke([world(x, v) for x, v in oval(0, 0, r, 5)])
    face.stroke([world(-5, 0), world(5, 0)])
    face.rect(8, 15, 63, 25, 3, EDGE)
    face.stroke([(71, 40), (100, 40), (100, 15), (71, 15)], EDGE, dashed=True)
    for a, b in ((15, 26), (31, 39), (44, 59), (64, 93)):
        face.rules(a, 28, [b - a], ink=BOLD)
    face.stroke([(71, 17), (71, 24)], EDGE)
    face.stroke([(71, 32), (71, 38)], EDGE)
