from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import identity_card

DESCRIPTION = "A standing ID card shows a featureless portrait silhouette and carries a slash badge."


def draw(s):
    face = identity_card(s)
    head = oval(21, 29, 6, 7, -22, 202, 30)
    silhouette = [*head, (16, 24), (18, 21), (13, 19), (11, 15), (11, 12),
                  (31, 12), (31, 15), (29, 19), (24, 21), (26, 24), head[0]]
    s.line([face(x, z) for x, z in silhouette], EDGE)
    for z, length in ((27, 14), (18, 21)):
        s.line([face(42, z), face(42 + length, z)], DETAIL)
    badge(s, "slash", 69, -3, 43, 10)
