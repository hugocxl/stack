from geometry import EDGE
from scenes.redraws._w4 import standing_card

DESCRIPTION = "A filter panel shows a funnel above a parent checkbox and two visibly indented child checkboxes."


def draw(s):
    face = standing_card(s, 89, 98, angle=-18, lean=.25, depth=7)
    face.outline([(11, 87), (28, 87), (22, 80), (22, 74),
                  (17, 72), (17, 80)], EDGE)
    face.rows(35, 81, (29,), ink=EDGE)
    face.line([(8, 66), (80, 66)])
    face.frame(12, 48, 12, 12, 2, EDGE)
    face.rows(31, 54, (28,), ink=EDGE)
    face.line([(18, 48), (18, 15), (31, 15)], EDGE)
    face.line([(18, 32), (31, 32)], EDGE)
    for v in (9, 26):
        face.frame(31, v, 12, 12, 2, EDGE)
        face.rows(50, v + 6, (21,), ink=EDGE)
