from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, typeset_a

DESCRIPTION = "Two mounted page proofs show the same letterform at two sizes and large lines reflowing into a narrower measure."


def draw(s):
    wide = Surface(s, (0, 0, 0), across=(.97, -.24))
    wide.plate(rounded(0, 0, 85, 66, 3), 6)
    typeset_a(wide, 9, 32, 25)
    wide.rules(33, 48, [42], ink=EDGE)
    wide.rules(33, 35, [32], ink=EDGE)
    wide.rules(9, 22, [58, 66, 51], gap=7)

    narrow = Surface(s, (82, -15, 0), across=(.97, -.24))
    narrow.plate(rounded(0, 0, 45, 66, 3), 6)
    typeset_a(narrow, 7, 44, 15)
    narrow.rules(7, 35, [29, 24, 29, 16], gap=6, ink=EDGE)
    narrow.rules(7, 9, [27])
