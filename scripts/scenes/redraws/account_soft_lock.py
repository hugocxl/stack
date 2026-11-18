from geometry import DETAIL, EDGE
from scenes.redraws._w5 import upright_card
from scenes.systems_shapes import bezel, lock

DESCRIPTION = "A profile card with an empty portrait frame and a lanyard slot carries a closed padlock at its upper-right corner."


def draw(s):
    upright_card(s, 78, 52, 5, 3.5)
    bezel(s, 28, 0, 42, 19, 4, DETAIL, 2)
    bezel(s, 9, 0, 10, 24, 25, EDGE, 2)
    for z, width in ((29, 20), (22, 24), (15, 16)):
        s.line([(41, 0, z), (41 + width, 0, z)], DETAIL)

    lock(s, 61, -1, 36, w=26, d=8, h=19)
