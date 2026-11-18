from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import classroom_chair, classroom_desk

DESCRIPTION = "Two school desks with chairs stand under a pair of opposing swap arrows."


def draw(s):
    classroom_desk(s, 0, 0)
    classroom_chair(s, 6, 27)
    classroom_desk(s, 48, 0)
    classroom_chair(s, 54, 27)
    arrow(s, [(13, 1, 40), (30, 1, 50), (49, 1, 56), (66, 1, 54)], EDGE, head=6)
    arrow(s, [(65, 1, 42), (48, 1, 43), (29, 1, 38), (14, 1, 29)], EDGE, head=6)
