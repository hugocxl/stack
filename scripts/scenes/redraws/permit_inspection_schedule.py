from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import board, closed_outline, rule, upright_face
from scenes.redraws.homebuyer_closing_packet import house_emblem

DESCRIPTION = "An inspection clipboard shows a house outline and appointment rows with a clock badge on its corner."


def draw(s):
    point = board(s, 67, 84, run=.40, depth=10)
    upright_face(s, point, [(6, 7), (61, 7), (61, 76), (6, 76)], 1.3)
    upright_face(s, point, [(21, 69), (21, 79), (28, 79), (30, 84),
                            (38, 84), (40, 79), (47, 79), (47, 69)], 3)
    house_emblem(s, point, 32, 53, 16)
    for z in (16, 27):
        closed_outline(s, point, [(14, z), (19, z), (19, z + 5), (14, z + 5)], EDGE)
        rule(s, point, 25, z + 2.5, 21)
    x, y, z = point(66, 68)
    badge(s, "clock", x + 6, y + 1, z + 2, 15)
