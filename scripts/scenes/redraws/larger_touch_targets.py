from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A centered tap ripple sits well inside an oversized button on a smartphone."


def draw(s):
    phone = Surface(s, (0, 0, 1), rise=(-.20, .98), back=(0, -.98, -.20))
    phone.plate(rounded(0, 0, 56, 88, 8), 8)
    phone.rect(4, 5, 48, 78, 5, DETAIL)
    phone.rules(22, 77, [12], ink=EDGE)
    phone.rules(21, 11, [14])
    phone.rect(9, 23, 38, 44, 7, EDGE)
    phone.oval(28, 45, 12, 12, DETAIL)
    phone.oval(28, 45, 7, 7, EDGE)
    phone.oval(28, 45, 2.8, 2.8, BOLD)
