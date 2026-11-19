from geometry import DETAIL, EDGE, rounded
from scenes.redraws.recycling import bin_body

DESCRIPTION = "A folded newspaper enters the top slot of a bin marked with three chasing recycling arrows."


def draw(s):
    bin_body(s)
    s.box(-28, -21, 55, 56, 43, 5, 2.6)
    # Build the slot as an opening in a thick lid top.
    opening = [(-21, -4, 61), (21, -4, 61), (21, 7, 61), (-21, 7, 61)]
    s.face([(x, y, 61) for x, y in rounded(-27, -20, 54, 41, 2)], EDGE, openings=[opening])
    s.face([(-18, 4, 61), (-18, -13, 87), (18, -13, 87), (18, 4, 61)], EDGE)
    s.face([(-17, 5, 61), (-17, -10, 85), (19, -10, 85), (19, 5, 61)], EDGE)
    for fraction in (.35, .6, .8):
        y, z = -10 + 15 * fraction, 85 - 24 * fraction
        s.line([(-12, y, z), (1, y, z)], DETAIL)
    s.face([(5, -6, 78.6), (14, -6, 78.6), (14, -.5, 69.8), (5, -.5, 69.8)], DETAIL)
