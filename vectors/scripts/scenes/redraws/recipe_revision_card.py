from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import cutlery, printed_stroke

DESCRIPTION = "A tabbed recipe card has a fork-and-knife header, ruled steps, and a refresh badge at one corner."


def draw(s):
    face = lambda x, z: (x, 9 - .49 * z, z - 4)
    outline = [(0, 4), (65, 4), (65, 42), (29, 42),
               (25, 51), (4, 51), (0, 47)]
    front = [face(x, z) for x, z in outline]
    back = [(x, y - 4, z) for x, y, z in front]
    s.face(back)
    s.face([front[1], back[1], back[2], front[2]])
    s.face(front, EDGE)
    cutlery(s, face, 14, 37, .95)
    printed_stroke(s, face, [(27, 36), (46, 36)], EDGE)
    printed_stroke(s, face, [(7, 27), (55, 27)], DETAIL)
    for z, width in ((21, 34), (15, 26), (9, 30)):
        printed_stroke(s, face, [(9, z), (11, z)], EDGE)
        printed_stroke(s, face, [(16, z), (16 + width, z)], DETAIL)
    badge(s, "refresh", *face(63, 42), 10)
