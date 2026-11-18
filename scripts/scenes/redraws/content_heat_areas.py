from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w2 import laptop, outline

DESCRIPTION = "A laptop displays a web page with concentric attention contours around its main link."


def draw(s):
    point = laptop(s, 112, 78)
    s.line([point(6, 72), point(106, 72)], EDGE)
    for x in (12, 19, 26):
        s.line([point(x, 77), point(x + 2, 77)], DETAIL)
    for z, length in ((61, 33), (52, 28), (44, 31), (36, 22), (28, 27)):
        s.line([point(14, z), point(14 + length, z)], EDGE if z == 61 else DETAIL)
    for r, ink in ((26, DETAIL), (19, EDGE), (12, BOLD)):
        s.line([point(x, z) for x, z in oval(73, 41, r, r, count=48)], ink)
    outline(s, 67, 0, 38, 12, 6, 2, EDGE)
