from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import standing_card

DESCRIPTION = "A power drill pictogram and a clock badge identify the highlighted pickup window on a standing appointment card."


def draw(s):
    card = standing_card(s, 96, 55, angle=-25, lean=.55, depth=7)
    card.line([(0, 44), (96, 44)], DETAIL)
    drill = [(9, 40), (27, 40), (31, 37), (36, 37), (36, 32), (25, 32),
             (20, 17), (24, 17), (24, 11), (7, 11), (7, 17),
             (12, 17), (16, 32), (9, 32)]
    card.outline(drill)
    card.line([(36, 34.5), (43, 34.5)], EDGE)
    card.line([(24, 29), (27, 29), (27, 26), (23, 26)], DETAIL)
    card.line([(9, 17), (22, 17)], DETAIL)
    card.frame(47, 13, 40, 22, 3, EDGE)
    card.rows(54, 24, (26,), ink=EDGE)
    for u in (54, 80):
        card.line([(u, 21), (u, 27)], EDGE)
    badge(s, "clock", *card.at(94, 36), 13)
