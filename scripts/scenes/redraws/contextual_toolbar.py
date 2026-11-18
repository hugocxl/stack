from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w3 import Surface, selection_handle

DESCRIPTION = "A floating three-button toolbar points directly to the selection bounds around a single object on a tilted canvas."


def draw(s):
    canvas = Surface(s, (0, 20, 0), rise=(-.68, .74), back=(0, -.74, -.68))
    canvas.plate(rounded(0, 0, 87, 66, 5), 7)
    canvas.rect(21, 11, 45, 33, 1, EDGE)
    canvas.oval(43.5, 27.5, 12, 11, EDGE)
    for x in (21, 66):
        for z in (11, 44):
            selection_handle(canvas, x, z, 5)

    bar = Surface(s, canvas.point(9, 49, -4))
    bar.plate([(0, 3), (29, 3), (35, -3), (41, 3), (69, 3),
               (72, 6), (72, 23), (69, 26), (3, 26), (0, 23)], 5, BOLD)
    for x in (24, 48):
        bar.stroke([(x, 7), (x, 22)], DETAIL)
    bar.rect(7, 10, 10, 9, 1, EDGE)
    bar.stroke([(10, 22), (20, 22), (20, 14)], EDGE)
    glyph(s, "plus", *bar.point(36, 14), 6, EDGE)
    for x in (54, 60, 66):
        bar.oval(x, 14, .9, .9, EDGE)
