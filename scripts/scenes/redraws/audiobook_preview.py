from geometry import EDGE
from scenes.redraws._w4 import closed_book, play_mark

DESCRIPTION = "A closed hardback has a large play triangle inset into its cover."


def draw(s):
    book = closed_book(s, angle=-28)
    book.frame(19, 23, 44, 46, 5, EDGE)
    play_mark(book, 40, 46, 15)
