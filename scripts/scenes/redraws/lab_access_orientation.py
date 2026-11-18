from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import manual

DESCRIPTION = "A lab access booklet displays an entry credential and an upper-corner check badge."


def draw(s):
    cover = manual(s)
    cover.rect(20, 33, 43, 31, 4, EDGE)
    cover.rect(27, 51, 11, 7, 2, EDGE)
    cover.rules(43, 54, [14, 9], gap=5)
    cover.rules(27, 43, [29, 20], gap=5)
    cover.rect(36, 62, 12, 5, 2, EDGE)
    cover.rules(21, 22, [39, 28], gap=8)
    badge(s, "check", 76, 0, 89, 13)
