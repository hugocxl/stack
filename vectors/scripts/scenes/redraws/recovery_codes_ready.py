from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import code_rows, file_card

DESCRIPTION = "A folded-corner backup-code sheet carries three rows of grouped marks and a check badge."


def draw(s):
    file_card(s, -26, 0, w=52, h=65, depth=4)
    s.line([(-18, 0, 53), (3, 0, 53)], EDGE)
    s.line([(-18, 0, 46), (19, 0, 46)], DETAIL, dashed=True)
    code_rows(s, -17, 0, 35)
    badge(s, "check", 28, 0, 61, 12.5)
