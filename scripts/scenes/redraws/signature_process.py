from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import standing_card

DESCRIPTION = "A thick process card links a circle, a diamond, and a square in three successive steps."


def draw(s):
    face = standing_card(s, 111, 64, angle=-8, lean=.67, depth=8)
    face.rows(11, 51, (39,), ink=EDGE)
    face.oval(20, 31, 8, 8, EDGE)
    face.outline([(55, 21), (65, 31), (55, 41), (45, 31)], EDGE)
    face.frame(82, 23, 16, 16, 1.4, EDGE)
    for a, b in ((31, 42), (67, 79)):
        arrow(s, [face.at(a, 31), face.at(b, 31)], head=3.5)
    for u in (14, 49, 84):
        face.rows(u, 14, (12,))
