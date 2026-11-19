from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import file_card
from scenes.systems_shapes import bezel

DESCRIPTION = "A folded-corner template sheet shows a preformatted header and columns with a plus badge on its corner."


def draw(s):
    file_card(s, -31, 0, w=62, h=67, depth=6)
    s.line([(-23, 0, 54), (6, 0, 54)], EDGE)
    s.line([(-23, 0, 45), (20, 0, 45)], DETAIL)
    bezel(s, -23, 0, 14, 23, 23, EDGE, 1)
    for z, end in ((35, 21), (28, 17), (21, 22), (14, 14)):
        s.line([(6, 0, z), (end, 0, z)], DETAIL)
    badge(s, "plus", 30, 0, 11, 12)
