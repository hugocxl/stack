from geometry import DETAIL, EDGE
from scenes.redraws._w1 import clipboard
from scenes.systems_shapes import bezel

DESCRIPTION = "A clipped wholesale order form shows a loaded pallet beside three case quantity marks."


def draw(s):
    clipboard(s)
    s.line([(-18, 0, 39), (16, 0, 39)], EDGE)
    s.line([(-18, 0, 34), (2, 0, 34)], DETAIL)

    # Side elevation of a loaded pallet with two fork openings.
    for x in (-19, -9):
        bezel(s, x, 0, 16, 10, 12, EDGE, .6)
        s.line([(x + 5, 0, 24), (x + 5, 0, 28)], DETAIL)
    bezel(s, -21, 0, 12, 24, 4, EDGE, .5)
    for x in (-20, -10, 0):
        s.line([(x, 0, 12), (x, 0, 9), (x + 2, 0, 9), (x + 2, 0, 12)], EDGE)

    s.line([(6, 0, 10), (6, 0, 29)], DETAIL)
    for x in (10, 15, 20):
        s.line([(x, 0, 16), (x, 0, 25)], EDGE)
    s.line([(-20, 0, 6), (22, 0, 6)], DETAIL)
