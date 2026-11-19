from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import Surface, paper

DESCRIPTION = "A tabbed source dossier holds a ruled record and carries a linked-reference tab."


def draw(s):
    back = paper(s, 75, pitch=.58, angle=1, depth=7)
    back.slab([(0, 12), (0, 5), (4, 1), (35, 1), (44, 12),
               (90, 12), (90, 75), (0, 75)], 4)
    record = Surface(s, lambda u, v: (u, v*.84, 11 + (75-v)*.55))
    record.slab(rounded(10, 9, 70, 60, 2), 2)
    record.rows(18, 17, (34,), ink=EDGE)
    record.rows(18, 25, (46, 38, 43))
    front = Surface(s, lambda u, v: (u, v*.84, 13 + (75-v)*.39))
    front.slab(rounded(0, 35, 90, 40, 3), 3)
    front.rows(10, 48, (31, 22))
    front.slab([(58, 44), (89, 44), (99, 54), (89, 64), (58, 64)], 2, EDGE)
    front.line([(73, 53), (70, 53), (65, 57), (65, 60), (69, 61), (75, 57)], BOLD)
    front.line([(79, 55), (86, 51), (86, 48), (82, 47), (75, 51)], BOLD)
    front.line([(72, 57), (81, 51)], EDGE)
