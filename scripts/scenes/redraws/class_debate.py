from geometry import EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "Two equal-sized speech bubbles turn toward each other across a narrow gap."


def draw(s):
    outline = [(5, 0), (23, 0), (36, -10), (34, 0), (42, 0),
               (47, 5), (47, 28), (42, 33), (5, 33), (0, 28), (0, 5)]
    for origin, mirrored in (((49, 0, 35), True), ((0, 8, 27), False)):
        face = Surface(s, origin)
        face.plate([(47 - x if mirrored else x, v) for x, v in outline], 4)
        face.rules(8 if mirrored else 11, 22, [28], ink=EDGE)
        face.rules(8 if mirrored else 11, 13, [21])
