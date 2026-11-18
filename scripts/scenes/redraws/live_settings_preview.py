from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, flat

DESCRIPTION = "A laptop previews a sample card whose rounded corners reflect the position of a slider beside it."


def draw(s):
    base = flat(s, 0, 57, 4)
    base.plate(rounded(0, 0, 109, 57, 5), 4)
    for v in (22, 28, 34, 40):
        base.rules(14, v, [81])
    base.rect(41, 6, 27, 11, 3)

    screen = Surface(s, (0, 7, 4), rise=(-.20, .98), back=(0, -.98, -.2))
    screen.plate(rounded(0, 0, 109, 69, 5), 7)
    screen.rect(6, 6, 97, 57, 3, EDGE)
    screen.stroke([(69, 6), (69, 63)], DETAIL)
    screen.rect(13, 15, 49, 36, 13, EDGE)
    screen.rules(22, 38, [24], ink=EDGE)
    screen.rules(22, 31, [29, 20], gap=7)
    screen.rules(76, 49, [20], ink=EDGE)
    screen.rules(76, 28, [20], ink=EDGE)
    control = Surface(s, screen.point(92, 28, -2), rise=screen.rise, back=screen.back)
    control.plate(rounded(-4, -4, 8, 8, 3), 2, BOLD)
