from geometry import BOLD, EDGE
from scenes.commerce_objects import house
from scenes.redraws._w2 import closed_outline, face_arrow

DESCRIPTION = "A rising arrow sits beside a stair of efficiency bars on the gable of a small house."


def draw(s):
    house(s)

    def gable(u, v):
        return 20.05, 11 - u, v

    for z, length in ((4.7, 9), (9.6, 13), (14.5, 17)):
        closed_outline(s, gable, [(0, z - 1.7), (length - 2.5, z - 1.7),
                                  (length, z), (length - 2.5, z + 1.7),
                                  (0, z + 1.7)], EDGE)
    face_arrow(s, gable, [(21, 4.7), (21, 17.5)], BOLD, head=4.8)
