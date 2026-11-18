from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "An interlocking chain heads an expanded link card with a landscape thumbnail and page title lines."


def draw(s):
    card = Surface(s, (0, 0, 0), rise=(-.35, .94), back=(0, -.94, -.35),
                   across=(.97, -.24))
    card.plate(rounded(0, 0, 104, 69, 7), 8)
    card.rules(0, 46, [104], ink=EDGE)
    card.rules(43, 57, [49], ink=EDGE)
    photo_art(card, 9, 8, 44, 30)
    card.rules(61, 32, [31], ink=EDGE)
    card.rules(61, 23, [32, 23], gap=7)

    for x, start, end in ((16, 30, 310), (27, 210, 490)):
        card.stroke(oval(x, 57, 9, 5.5, start, end, 32), BOLD)
    card.stroke([(20, 54), (23, 60)], EDGE)
