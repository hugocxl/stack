from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import identity_card, identity_details, panel

DESCRIPTION = "A standing profile card carries a star-marked role tag clipped to its header."


def draw(s):
    face = identity_card(s)
    identity_details(s, face)
    tag = lambda x, z: (x, -.5, z)
    panel(s, [(54, 49), (61, 56), (84, 56), (84, 41), (61, 41)],
          tag, 2.4)
    s.line([tag(x, z) for x, z in oval(61, 49, 2, 2, count=20)], DETAIL)
    s.tube([face(52, 47), (52, -6, 53), (56, -2, 53), (60, .5, 49)],
           1.1, EDGE)
    glyph(s, "star", 74, -.5, 48.5, 7.2, EDGE)
