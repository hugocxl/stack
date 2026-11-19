from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "An upward arrow badge sits at the opening of a tabbed artist portfolio containing a landscape print."


def draw(s):
    back = Surface(s, (0, -14, 0))
    back.plate([(0, 0), (92, 0), (92, 63), (36, 63),
                (29, 73), (4, 73), (0, 68)], 5)
    print_face = Surface(s, (12, -6, 12), rise=(-.19, 1))
    print_face.plate(rounded(0, 0, 70, 67, 3), 2)
    photo_art(print_face, 7, 27, 56, 33)
    s.face([(92, -14, 0), (92, -.5, 0), (92, 3.9, 39), (92, -14, 49)])
    s.line([(92, -7, 45), (92, -7, 3)])
    front = Surface(s, (0, 0, 0), rise=(.10, 1))
    front.plate([(0, 0), (92, 0), (92, 39), (86, 44), (6, 44), (0, 39)], 5)
    front.rect(33, 16, 26, 10, 2, EDGE)
    badge(s, "up", 92, 5, 42, 15)
