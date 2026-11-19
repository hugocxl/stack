from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w4 import standing_card

DESCRIPTION = "An identification card shows a fingerprint panel and an attached verification check badge."


def draw(s):
    card = standing_card(s, 96, 63, angle=-34, lean=.34, depth=5)
    card.frame(38, 52, 20, 5, 2, EDGE)
    card.frame(9, 10, 34, 37, 3)
    for radius, start, end in ((12, -40, 210), (8.5, -74, 225), (5, -80, 205)):
        card.line(oval(26, 28, radius, radius*1.23, start, end, count=32), EDGE)
    card.rows(52, 40, (32,), ink=EDGE)
    card.rows(52, 30, (24, 29), step=-9)
    badge(s, "check", *card.at(91, 13), 14)
