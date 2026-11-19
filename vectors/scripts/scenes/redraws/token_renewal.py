from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import lens_outline, panel, rect

DESCRIPTION = "A rounded security token has a passcode display, a button, and a refresh badge."


def draw(s):
    face = lambda x, z: (x, -.25 * z, z)
    panel(s, rounded(0, 0, 39, 60, 13), face, 7)
    lens_outline(s, face, 19.5, 52, 3.4, EDGE)
    rect(s, face, 6, 29, 27, 15, 2.3)
    for x in (11, 17, 23, 28):
        s.line([face(x, 35), face(x + 2, 35)], EDGE)
    lens_outline(s, face, 19.5, 16, 4.5, DETAIL)
    badge(s, "refresh", *face(38, 49), 12)
