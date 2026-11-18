from geometry import BOLD, EDGE
from scenes.redraws._w3 import cover_cap, sheet

DESCRIPTION = "A lesson handout has a mortarboard heading, a framed exercise diagram and short instruction lines."


def draw(s):
    face = sheet(s, 78, 93, rise=(-.47, .88))
    cover_cap(face, 21, 75, 21)
    face.rules(37, 75, [24], ink=BOLD)
    face.rules(37, 66, [19])
    face.rect(12, 27, 54, 30, 2, EDGE)
    face.stroke([(20, 34), (28, 49), (35, 34)], EDGE, closed=True)
    face.oval(51, 41, 7, 7, EDGE)
    face.rules(12, 19, [48, 39], gap=8)
