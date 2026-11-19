from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import standing_card

DESCRIPTION = "A standing meal-plan card shows three plate-and-cutlery slots and carries a starred save badge."


def draw(s):
    card = standing_card(s, 101, 66, angle=-30, lean=.48, depth=8)
    for u in (37, 67):
        card.line([(u, 13), (u, 49)])
    for u in (22, 52, 82):
        card.oval(u, 33, 6.5, 6.5, EDGE)
        card.line([(u - 10.5, 27), (u - 10.5, 40)], EDGE)
        card.line([(u + 10.5, 27), (u + 10.5, 40)], EDGE)
        card.line([(u - 12, 40), (u - 12, 36), (u - 9, 36), (u - 9, 40)])
        card.rows(u - 8, 18, (16,))
    badge(s, "star", *card.at(101, 59), 15)
