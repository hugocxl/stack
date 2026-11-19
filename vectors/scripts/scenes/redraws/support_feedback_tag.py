from geometry import DETAIL, EDGE
from scenes.redraws._w4 import bezier_path, front_surface, printed_glyph, speech_bubble

DESCRIPTION = "A rating speech bubble carries a hanging feedback tag at its upper corner."


def draw(s):
    bubble = speech_bubble(s)
    for u in (21, 40, 59):
        printed_glyph(bubble, "star", u, 28, 9.5, EDGE)
    tag = front_surface(s, angle=-35, y=14, z=7)
    tag.slab([(91, 24), (104, 29), (116, 23), (126, 3), (100, -9),
              (88, 14)], 3)
    tag.oval(101, 20, 2.6, 2.6, EDGE)
    tag.line([(99, 9), (116, 15)], DETAIL)
    s.tube(bezier_path(bubble.at(80, 52), ((98, -21, 66),
                       (104, -28, 44), tag.at(101, 21))), 1.25)
