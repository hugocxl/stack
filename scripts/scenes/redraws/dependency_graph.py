from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import software_package

DESCRIPTION = "A root software package points to two dependent packages, and a third arrow links the dependents."


def draw(s):
    root, left, right = (-42, -42, 7), (-29, 38, 7), (38, -29, 7)
    for start, end, progress in ((root, left, .61), (root, right, .62), (left, right, .72)):
        stop = tuple(a + (b - a) * progress for a, b in zip(start, end))
        arrow(s, [start, stop], EDGE, head=9)
        s.line([stop, end], EDGE)

    software_package(s, *root[:2], 0, .66)
    software_package(s, *right[:2], 0, .59)
    software_package(s, *left[:2], 0, .59)
