from geometry import EDGE, GUIDE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, component_art, selection_handle

DESCRIPTION = "A selection boundary groups three thick component diamonds and carries a plus badge on its corner."


def draw(s):
    frame = Surface(s, (0, 0, 0), rise=(-.65, .76), back=(0, -.76, -.65),
                    across=(.98, -.2))
    frame.stroke([(0, 0), (96, 0), (96, 72), (0, 72), (0, 0)], GUIDE, dashed=True)
    for x, v in ((48, 51), (24, 22), (72, 22)):
        tile = Surface(s, frame.point(x, v, -4), rise=frame.rise, back=frame.back,
                       across=frame.across)
        tile.plate([(0, 15), (19, 0), (0, -15), (-19, 0)], 5, EDGE)
        component_art(tile, 0, 0, 15, 12, EDGE)
    for x, v in ((0, 0), (96, 0), (0, 72)):
        selection_handle(frame, x, v, 5)
    badge(s, "plus", *frame.point(96, 70, -4), 14)
