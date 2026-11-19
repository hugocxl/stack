from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A clock badge sits on the delivery label of a pallet loaded with strapped construction timbers."


def timber_pallet(s):
    """Draw the construction delivery with its label on the exposed end."""
    for y in (0, 24, 48):
        s.box(0, y, 0, 81, 7, 7, 1)
    for x in (0, 20, 40, 60, 75):
        s.box(x, 0, 7, 7, 55, 5, 1)
    for z in (12, 21, 30):
        s.box(4, 3, z, 74, 49, 9, 1)
        for y in (16, 28, 40):
            s.line([(78, y, z + .6), (78, y, z + 8.4)], DETAIL)
    for y in (16, 28, 40):
        s.line([(4, y, 39), (78, y, 39)], DETAIL)
    for x in (19, 56):
        for edge in (x, x + 4):
            s.line([(edge, 3, 39), (edge, 52, 39), (edge, 52, 12)], EDGE)
    s.face([(78.5, 9, 24), (78.5, 26, 24), (78.5, 26, 35), (78.5, 9, 35)], EDGE)
    s.line([(78.5, 12, 30), (78.5, 21, 30)], DETAIL)


def draw(s):
    timber_pallet(s)
    badge(s, "clock", 88, 6, 41, 13)
