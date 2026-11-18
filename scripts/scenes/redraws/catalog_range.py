from geometry import EDGE
from scenes.redraws._w4 import camera_emblem, open_book

DESCRIPTION = "An open product catalogue displays silhouettes of a bottle, a camera, and a lamp in three product areas."


def draw(s):
    left, right = open_book(s)
    left.rows(9, 12, (40,), ink=EDGE)
    left.outline([(19, 50), (19, 37), (23, 33), (23, 26), (33, 26), (33, 33),
                  (37, 37), (37, 50)], EDGE)
    left.line([(19, 41), (37, 41)])
    left.rows(19, 58, (18, 12), step=5)
    right.line([(70, 38), (117, 38)])
    camera_emblem(right, 78, 13, 22)
    right.rows(83, 33, (16,))
    right.outline([(81, 56), (87, 45), (97, 45), (103, 56)], EDGE)
    right.line([(92, 56), (92, 64)], EDGE)
    right.rows(84, 64, (16,), ink=EDGE)
