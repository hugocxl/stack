from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import cover_cap, manual

DESCRIPTION = "A tabbed teaching resource booklet with a mortarboard on its cover carries a check badge."


def draw(s):
    for v in (19, 39, 59):
        s.box(76, -13, v, 14, 7, 12, 1)
    cover = manual(s, 77, 83)
    cover_cap(cover, 42, 60, 40)
    cover.rules(19, 36, [42], ink=EDGE)
    cover.rules(19, 26, [32, 37], gap=7)
    badge(s, "check", 74, 0, 79, 14)
