from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import file_card

DESCRIPTION = "A folded-corner draft sheet carries two short written lines and a check badge."


def draw(s):
    file_card(s, -26, 0, w=52, h=64, depth=4)
    s.line([(-16, 0, 40), (16, 0, 40)], EDGE)
    s.line([(-16, 0, 29), (8, 0, 29)], DETAIL)
    badge(s, "check", 27, 0, 10, 13)
