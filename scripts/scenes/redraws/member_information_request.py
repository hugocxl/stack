from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, question, speech_outline
from scenes.redraws.introduction_buddy import avatar

DESCRIPTION = "A question-mark speech bubble overlaps the upper corner of a membership profile card."


def draw(s):
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, 89, 57, 6), 5)
    face.rect(10, 10, 32, 35, 4)
    avatar(face, 26, 27, 27)
    face.rules(49, 23, [29], ink=EDGE)
    face.rules(49, 15, [22])
    bubble = Surface(s, (0, 7, 0))
    bubble.plate(speech_outline(60, 34, 40, 37), 4)
    question(bubble, 80, 54, 24, aligned=True)
