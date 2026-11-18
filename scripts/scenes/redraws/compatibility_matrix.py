from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_check

DESCRIPTION = "A compatibility chart puts a monitor, tablet, and phone above columns of checked and empty cells."


def draw(s):
    matrix = Surface(s, (0, 0, 0), rise=(-.33, .94), across=(.98, -.22))
    matrix.plate(rounded(0, 0, 108, 81, 6), 8)
    for x in (40, 68):
        matrix.stroke([(x, 7), (x, 74)], DETAIL)
    for v in (28, 50):
        matrix.rules(10, v, [88], ink=EDGE)

    matrix.rect(14, 58, 22, 14, 2, EDGE)
    matrix.stroke([(25, 58), (25, 54), (20, 54), (30, 54)], EDGE)
    matrix.rect(46, 56, 17, 19, 2, EDGE)
    matrix.rect(78, 55, 11, 21, 2, EDGE)
    matrix.rules(81, 58, [5], ink=DETAIL)
    for x, v in ((25, 39), (54, 39), (83, 39), (25, 18), (83, 18)):
        printed_check(matrix, x, v, 9)
