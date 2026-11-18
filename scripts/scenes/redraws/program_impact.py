from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "A finished community house carries a check badge at its roof corner."


def community_house(s, *, door=True):
    """Draw the shared gable house, with its long front wall facing the viewer."""
    s.box(-29, -18, 0, 58, 36, 34, 1.1)
    s.face([(29, -18, 34), (29, 18, 34), (29, 0, 55)], EDGE)
    s.face([(32, -21, 33), (32, 0, 57), (32, 21, 33),
            (32, 21, 36), (32, 0, 60), (32, -21, 36)], EDGE)
    s.face([(-32, 21, 33), (32, 21, 33), (32, 21, 36), (-32, 21, 36)], EDGE)
    s.face([(-32, 0, 60), (32, 0, 60), (32, 21, 36), (-32, 21, 36)], EDGE)
    if door:
        bezel(s, -8, 18, 1, 14, 21, EDGE, .7)
        s.line([(2, 18, 10), (3.5, 18, 10)], DETAIL)
    bezel(s, -24, 18, 13, 10, 10, DETAIL, .5)
    s.line([(29, -12, 15), (29, 1, 15), (29, 1, 24), (29, -12, 24), (29, -12, 15)], DETAIL)


def draw(s):
    community_house(s)
    bezel(s, 12, 18, 13, 11, 10, EDGE, .5)
    s.box(-11, 17, 0, 20, 7, 3, .9)
    badge(s, "check", 36, -10, 48, 11)
