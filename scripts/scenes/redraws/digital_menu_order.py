from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import device, printed_stroke, rect

DESCRIPTION = "A phone displays two restaurant dishes and an attached plus badge beside the selected menu row."


def draw(s):
    face = device(s, w=47, h=72)
    printed_stroke(s, face, [(9, 57), (29, 57)], EDGE)
    rect(s, face, 6.5, 31, 34, 21, 2, DETAIL)
    x, z = 16.5, 39
    printed_stroke(s, face, oval(x, z, 7, 6, 0, 180, 24), EDGE)
    printed_stroke(s, face, [(x - 8, z), (x + 8, z)], EDGE)
    printed_stroke(s, face, [(x, z + 6), (x, z + 8)], EDGE)
    printed_stroke(s, face, [(27, 43), (35, 43)], EDGE)
    printed_stroke(s, face, [(27, 38), (33, 38)], DETAIL)
    printed_stroke(s, face, [(9, 24), (24, 24)], EDGE)
    printed_stroke(s, face, [(9, 24), (12, 19), (21, 19), (24, 24)], DETAIL)
    printed_stroke(s, face, [(27, 23), (37, 23)], EDGE)
    printed_stroke(s, face, [(27, 17), (34, 17)], DETAIL)
    badge(s, "plus", *face(46, 40), 10)
