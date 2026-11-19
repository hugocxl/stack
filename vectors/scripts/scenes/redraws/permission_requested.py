from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws.page_moved import Surface

DESCRIPTION = "An upright access pass with a lanyard slot and a keyhole carries a clock badge."


def access_pass(s):
    face = Surface(s, (8, 0, 0), lean=.26, side=True)
    face.plate(rounded(0, 0, 57, 78, 7), 4)
    face.frame(18, 65, 21, 5, 2, EDGE)
    face.loop(oval(28.5, 43, 15, 15, count=36)[:-1], DETAIL)
    keyhole = oval(28.5, 46, 5, 5, -52, 232, 24)
    face.loop([*keyhole, (23.5, 34), (33.5, 34)], EDGE)
    face.line([(15, 16), (42, 16)])
    face.line([(20, 10), (37, 10)])
    return face


def draw(s):
    face = access_pass(s)
    badge(s, "clock", *face.point(57, 58), 13)
