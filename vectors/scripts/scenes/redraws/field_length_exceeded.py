from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import warning
from scenes.redraws._w3 import Surface

DESCRIPTION = "A text entry crosses the end boundary of its outlined field beside an attached warning triangle."


def draw(s):
    field = Surface(s, (0, 0, 0), rise=(-.34, .94), back=(0, -.94, -.34),
                    across=(.97, -.2))
    field.plate(rounded(0, 0, 85, 37, 5), 7)
    field.rect(6, 8, 73, 22, 3, DETAIL)
    field.rules(14, 19, [16], ink=EDGE)
    field.rules(36, 19, [14], ink=EDGE)
    field.rules(56, 19, [13], ink=EDGE)
    field.rules(73, 19, [27], ink=EDGE)
    field.stroke([(100, 13), (100, 25)], EDGE)
    warning(s, *field.point(87, -9, -5), 26)
