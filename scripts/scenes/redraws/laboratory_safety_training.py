from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import warning
from scenes.redraws._w3 import manual

DESCRIPTION = "A laboratory safety manual carries a large safety-goggles emblem and a warning triangle."


def draw(s):
    cover = manual(s)
    goggles = [(18, 40), (17, 48), (20, 55), (26, 58), (61, 58), (68, 55),
               (71, 49), (70, 41), (66, 36), (58, 33), (51, 35), (47, 41),
               (43, 43), (39, 41), (35, 35), (27, 33), (21, 36)]
    cover.stroke(goggles, BOLD, closed=True)
    for x in (22, 49):
        cover.stroke(rounded(x, 39, 16, 13, 4), EDGE, closed=True)
    cover.rules(23, 23, [37, 25], gap=7)
    warning(s, 63, .1, 65, 20)
