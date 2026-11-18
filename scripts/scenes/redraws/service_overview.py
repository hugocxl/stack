from geometry import EDGE
from scenes.redraws._w4 import open_book, support_mark, wrench_mark

DESCRIPTION = "An open service catalog lists three offerings marked with a wrench, a headset, and a cloud."


def draw(s):
    left, right = open_book(s)
    left.rows(13, 15, (37,), ink=EDGE)
    for v, width in ((30, 23), (47, 21), (63, 19)):
        left.frame(13, v - 3, 6, 6, 1, EDGE)
        left.rows(24, v, (width,), ink=EDGE)
        left.rows(24, v + 5, (width * .7,))

    wrench_mark(right, 77, 25, .48)
    support_mark(right, 77, 55, .52)
    right.line([(101, 57), (97, 55), (97, 50), (100, 48), (103, 49),
                (106, 45), (110, 45), (113, 50), (116, 50), (118, 53),
                (115, 57), (101, 57)], EDGE)
