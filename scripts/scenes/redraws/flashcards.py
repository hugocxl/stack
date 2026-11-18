from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, flashcard_stack, question

DESCRIPTION = "A question card lifts from a stack of flashcards and reveals the answer lines underneath."


def draw(s):
    answer = flashcard_stack(s)
    answer.rules(17, 35, [45, 53, 32], gap=10, ink=EDGE)
    lifted = Surface(s, answer.point(9, 51), rise=(.19, .98), back=(0, -.98, .19))
    lifted.plate(rounded(0, 0, 88, 50, 5), 2)
    question(lifted, 44, 24, 23, aligned=True)
