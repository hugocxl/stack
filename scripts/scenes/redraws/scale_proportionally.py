from geometry import BOLD, EDGE, GUIDE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface, selection_handle

DESCRIPTION = "A diagonal resize arrow connects matching corner handles on a selection and a larger dashed outline of the same proportions."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.54, .84), back=(0, -.84, -.54), across=(.97, -.24))
    face.stroke([(0, 0), (110, 0), (110, 80), (0, 80), (0, 0)], EDGE, dashed=True)
    face.plate(rounded(0, 0, 66, 48, 2), 5, EDGE)
    face.rect(11, 9, 44, 30, 2, GUIDE)
    selection_handle(face, 66, 48, 8)
    selection_handle(face, 110, 80, 8)
    p = face.point
    arrow(s, [p(72, 52), p(104, 75)], BOLD, head=10)
