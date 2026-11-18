from scenes.redraws._w3 import Surface, question, speech_outline
from scenes.redraws.artifact_conservation import museum_vase

DESCRIPTION = "A question-mark speech bubble sits at the shoulder of a museum vase."


def draw(s):
    museum_vase(s, 0, 0, 0)
    bubble = Surface(s, (0, 4, 0))
    bubble.plate(speech_outline(12, 38, 40, 33), 3)
    question(bubble, 32, 56, 22, aligned=True)
