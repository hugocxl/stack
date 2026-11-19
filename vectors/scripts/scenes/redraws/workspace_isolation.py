from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A small workspace window stands inside the dashed front boundaries of its own open-frame sandbox."


def draw(s):
    low, high = 0, 72
    a, b, c, d = (0, 0), (78, 0), (78, 65), (0, 65)

    def at(corner, z):
        return (*corner, z)

    for corner in (a, b, d):
        s.line([at(corner, low), at(corner, high)], DETAIL, dashed=True)
    s.line([at(b, low), at(a, low), at(d, low)], DETAIL, dashed=True)
    s.line([at(b, high), at(a, high), at(d, high)], EDGE, dashed=True)

    s.line([at(b, low), at(c, low), at(d, low)], BOLD, dashed=True)
    s.line([at(b, high), at(c, high), at(d, high)], BOLD, dashed=True)
    s.line([at(c, low), at(c, high)], BOLD, dashed=True)

    workspace = Surface(s, (11, 39, 12), across=(.97, -.18))
    workspace.plate(rounded(0, 0, 57, 43, 3), 5, EDGE)
    workspace.rules(0, 33, [57], ink=EDGE)
    workspace.rect(7, 6, 12, 20, 1)
    workspace.rect(25, 6, 25, 20, 1)
