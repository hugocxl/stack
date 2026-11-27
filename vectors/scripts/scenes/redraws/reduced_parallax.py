from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import display

DESCRIPTION = "A display shows a near ridge and a faint far ridge locked together, with a slash badge."


def draw(s):
    face = display(s, 108, 70, stand=False)
    s.line([face(u, v) for u, v in [(6, 30), (28, 50), (44, 38), (66, 56), (102, 34)]], DETAIL)
    s.line([face(u, v) for u, v in [(6, 14), (30, 34), (52, 22), (76, 40), (102, 18)]], EDGE)
    badge(s, "slash", 104, 0, 66, 12)
