from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, selection_handle

DESCRIPTION = "Two dotted alignment guides cross at the center of a selection with four corner handles."


def draw(s):
    canvas = Surface(s, (0, 0, 0), rise=(-.56, .83), back=(0, -.83, -.56))
    canvas.plate(rounded(0, 0, 111, 72, 6), 6)
    canvas.rect(30, 19, 51, 34, 2, EDGE)
    for x in (30, 81):
        for v in (19, 53):
            selection_handle(canvas, x, v)
    canvas.stroke([(9, 36), (102, 36)], EDGE, dashed=True)
    canvas.stroke([(55.5, 7), (55.5, 66)], EDGE, dashed=True)
    canvas.oval(55.5, 36, 3, 3, BOLD)
