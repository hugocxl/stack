from geometry import DETAIL, EDGE
from scenes.redraws._w4 import front_surface, printed_glyph, wrench_mark
from scenes.redraws._kit import badge

DESCRIPTION = "A looped equipment return tag has a printed return arrow and an attached due-time clock badge."


def draw(s):
    tag = front_surface(s, angle=-32, z=5, lean=.30)
    s.tube([tag.at(32, 67), tag.at(22, 81), tag.at(25, 89),
            tag.at(36, 91), tag.at(42, 84), tag.at(36, 71)], 1.55, DETAIL)
    tag.slab([(4, 0), (58, 0), (62, 4), (62, 61), (43, 76),
              (20, 76), (0, 61), (0, 4)], 5)
    tag.oval(32, 66, 4, 4, EDGE)
    s.tube([tag.at(32, 66), tag.at(34, 75), tag.at(36, 80)], 1.45, EDGE)
    wrench_mark(tag, 21, 43, .49)
    printed_glyph(tag, "back", 45, 43, 9)
    tag.frame(12, 11, 38, 15, 3)
    tag.rows(18, 18, (14,), ink=EDGE)
    badge(s, "clock", *tag.at(60, 24), 13)
