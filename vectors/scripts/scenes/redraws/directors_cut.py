from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, upright

DESCRIPTION = "An open clapperboard carries an editing-splice emblem across its slate."


def draw(s):
    width = 100
    face = Surface(s, lambda x, z: (x, 10, z))
    upright(s, rounded(0, 0, width, 69, 3), 10, 10)
    face.line([(0, 56), (width, 56)], EDGE)
    for x in range(2, 86, 17):
        face.line([(x, 56), (x + 12, 69)], EDGE)

    # The upper clapstick pivots around the left end of the fixed stick.
    stick = Surface(s, lambda u, v: (u*.947 - v*.321, 10, 65 + u*.321 + v*.947))
    corners = [(0, 0), (100, 0), (100, 13), (0, 13)]
    outline = [(x, z) for u, v in corners for x, _, z in (stick.at(u, v),)]
    upright(s, outline, 10, 10)
    for u in range(7, 91, 17):
        stick.line([(u, 0), (u + 10, 13)], EDGE)
    face.oval(5, 70, 2.1, 2.1, DETAIL)

    # Two lengths of perforated film meet at a diagonal splice.
    left = [(17, 16), (46, 16), (55, 43), (17, 43)]
    right = [(52, 16), (83, 16), (83, 43), (61, 43)]
    for strip in (left, right):
        face.outline(strip, BOLD)
    for u in (23, 33, 67, 77):
        for z in (22, 37):
            face.frame(u - 2.3, z - 1.4, 4.6, 2.8, .4, EDGE)
    face.line([(17, 28), (49, 28)], DETAIL)
    face.line([(57, 31), (83, 31)], DETAIL)
