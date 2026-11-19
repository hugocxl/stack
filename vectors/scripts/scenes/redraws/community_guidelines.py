from geometry import EDGE
from scenes.redraws._w3 import book, speech_outline

DESCRIPTION = "A casebound community rules booklet carries a speech emblem and three rules on its cover."


def draw(s):
    face = book(s, w=68, h=81, depth=13)
    face.stroke(speech_outline(20, 42, 35, 26), EDGE, closed=True)
    face.rules(27, 59, [20, 15], gap=7, ink=EDGE)
    for v, width in ((28, 28), (21, 22), (14, 25)):
        face.rules(19, v, [3], ink=EDGE)
        face.rules(26, v, [width])
