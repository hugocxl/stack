from geometry import DETAIL, EDGE, GUIDE, rounded
from scenes.redraws._w3 import Surface, photo_art, selection_handle

DESCRIPTION = "A single selection frame encloses a landscape tile, a text tile, and a pill-shaped button."


def draw(s):
    frame = Surface(s, (0, 0, 0), rise=(-.68, .73), back=(0, -.73, -.68),
                    across=(.97, -.24))
    for x, v, w, h, radius in ((7, 10, 41, 47, 4), (57, 33, 47, 24, 4), (57, 10, 37, 15, 7)):
        block = Surface(s, frame.point(x, v, -5), rise=frame.rise, back=frame.back, across=frame.across)
        block.plate(rounded(0, 0, w, h, radius), 5)
        if x == 7:
            photo_art(block, 5, 8, 31, 31)
        elif v == 33:
            block.rules(6, 17, [24, 33, 27], gap=5)
        else:
            block.rules(11, 8, [15], ink=EDGE)
    frame.stroke([(0, 0), (111, 0), (111, 64), (0, 64), (0, 0)], GUIDE, dashed=True)
    for x, v in ((0, 0), (0, 64), (111, 64), (111, 0)):
        selection_handle(frame, x, v, 5)
