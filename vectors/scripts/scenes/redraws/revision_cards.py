from scenes.redraws._w3 import flashcard_stack, question

DESCRIPTION = "A stack of rounded study cards shows a large question mark on the top card."


def draw(s):
    face = flashcard_stack(s)
    question(face, 44, 27, 31, aligned=True)
