from geometry import DETAIL, EDGE
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "An open family-size takeaway carton holds three separated servings."


def draw(s):
    lid = lambda x, z: (x, -.57 * (z - 14), z)
    panel(s, [(0, 14), (68, 14), (70, 43), (65, 49), (3, 49), (-2, 43)], lid, 2)
    rect(s, lid, 6, 19, 56, 23, 3, DETAIL)
    s.box(2, 3, 0, 64, 45, 4, 2)
    s.face([(0, 0, 14), (68, 0, 14), (66, 5, 4), (2, 5, 4)], DETAIL)
    s.box(2, 1, 4, 3, 47, 10, .7)
    for x in (7, 28, 49):
        bread = [(x, 11), (x + 13, 19), (x + 12, 22), (x, 30), (x - 1, 13)]
        s.solid(bread, 4, 13, crease=False)
        s.line([(a, b, 17) for a, b in bread + bread[:1]], EDGE)
        s.line([(x, 30, 11), (x + 12, 22, 11), (x + 13, 19, 11)], DETAIL)
        s.disk(x + 9, 37, 4, 4.4, 4.4, 6)
    for x in (23, 44):
        s.box(x, 1, 4, 2, 47, 10, .6)
    s.face([(68, 0, 14), (70, 49, 14), (66, 47, 4), (66, 5, 4)])
    s.face([(2, 47, 4), (66, 47, 4), (70, 49, 14), (42, 49, 14),
            (40, 51, 17), (28, 51, 17), (26, 49, 14), (0, 49, 14)])
