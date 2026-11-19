from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import capsule_mark, standing_card

DESCRIPTION = "A bound medication record shows a capsule emblem and entry lines with a clock badge on its outer edge."


def draw(s):
    book = standing_card(s, 70, 83, angle=-16, lean=.39, depth=12)
    book.line([(8, 2), (8, 81)], EDGE)
    capsule_mark(book, 42, 56, 15, BOLD)
    for v in (19, 27, 35):
        book.oval(24, v, 1.3, 1.3, EDGE)
        book.rows(31, v, (23,))
    badge(s, "clock", *book.at(70, 34), 17)
