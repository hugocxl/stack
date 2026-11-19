from geometry import DETAIL, EDGE
from scenes.redraws._w2 import card, magnifier, outline


DESCRIPTION = "A magnifier covers the command row on an action summary card."


def draw(s):
    card(s, 94, 67)
    s.line([(13, 0, 57), (60, 0, 57)], DETAIL)
    outline(s, 8, 0, 23, 74, 22, ink=EDGE)
    s.line([(23, 0, 41), (30, 0, 34), (23, 0, 27)], EDGE)
    s.line([(34, 0, 27), (42, 0, 27)], EDGE)
    s.line([(13, 0, 9), (44, 0, 9)], DETAIL)
    magnifier(s, 37, 3, 37, 21)
