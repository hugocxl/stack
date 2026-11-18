from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w2 import level_face, rule

DESCRIPTION = "Two audience circles share one stack of profile cards in their intersection."


def draw(s):
    for x in (38, 81):
        s.line([level_face(u, v) for u, v in oval(x, 42, 38, 34)], EDGE)
    for x, z in ((49, 31), (52, 27), (55, 23)):
        s.face([level_face(u, v) for u, v in ((x, z), (x + 16, z),
                (x + 16, z + 24), (x, z + 24))], EDGE)
    s.line([level_face(u, v) for u, v in oval(63, 39, 3.3, 3.3)], BOLD)
    rule(s, level_face, 59, 30, 8, DETAIL)
