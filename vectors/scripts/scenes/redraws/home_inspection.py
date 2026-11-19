from scenes.commerce_objects import house
from scenes.redraws._w2 import face_magnifier

DESCRIPTION = "An open magnifying glass frames the junction where a house's roof meets its front wall."


def draw(s):
    house(s)

    def lens(u, v):
        return 18 + .55*u, 16 - .45*u, 23 + .94*v

    face_magnifier(s, lens, 0, 0, 13, direction=(.68, -.73))
