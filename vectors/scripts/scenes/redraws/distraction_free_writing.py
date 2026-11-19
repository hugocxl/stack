from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "An open laptop shows a short paragraph and an insertion caret across a borderless writing screen."


def draw(s):
    s.box(0, 1, 0, 100, 37, 5, 4)
    keyboard = Surface(s, (0, 38, 5), rise=(-1, 0), back=(0, 0, -1))
    keyboard.rect(13, 16, 74, 15, 3)
    keyboard.rect(39, 5, 22, 8, 2)
    display = Surface(s, (0, 2, 5), rise=(-.23, .97), back=(0, -.97, -.23))
    display.plate(rounded(0, 0, 100, 71, 5), 5)
    display.rect(5, 5, 90, 61, 3, EDGE)
    display.rules(23, 48, [56, 49, 55, 31], gap=9, ink=EDGE)
    display.stroke([(58, 17), (58, 25)], BOLD)
