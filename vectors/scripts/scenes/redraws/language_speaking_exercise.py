from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, microphone, speech_outline

DESCRIPTION = "A tabletop speaking prompt shows a large microphone and one short line inside a speech bubble."


def draw(s):
    s.box(0, 0, 0, 98, 38, 5, 4)
    face = Surface(s, (0, 33, 5), rise=(-.27, .96), back=(0, -.96, -.27))
    face.plate(rounded(2, 0, 94, 61, 5), 8)
    microphone(face, 24, 28, 33, BOLD)
    face.stroke(speech_outline(46, 18, 40, 32), EDGE, closed=True)
    face.rules(53, 36, [24], ink=EDGE)
