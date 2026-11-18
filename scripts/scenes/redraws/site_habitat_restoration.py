from geometry import DETAIL, EDGE
from scenes.redraws._w1 import tree_crown

DESCRIPTION = "A young tree and new shoots share a cutaway patch of soil with exposed roots."


def draw(s):
    ground = [(-35, -27), (24, -27), (36, -15), (36, 18),
              (26, 26), (-30, 26), (-38, 18)]
    s.solid(ground, 0, 13, crease=False)
    s.face([(*p, 13) for p in ground], EDGE)
    root_fork = (-4, 26, 8)
    s.line([(-4, 26, 13), root_fork, (-16, 26, 7), (-24, 26, 4)], EDGE)
    s.line([root_fork, (7, 26, 5), (19, 26, 4)], DETAIL)
    s.line([root_fork, (-1, 26, 2)], DETAIL)
    for x, y, height in ((-23, 9, 8), (11, 13, 6), (25, 6, 8), (13, -10, 7), (-16, -10, 6)):
        s.line([(x - 4, y, 13 + .7 * height), (x - 2, y, 14 + .45 * height),
                (x, y, 13), (x + 2, y, 13 + .5 * height),
                (x + 5, y, 13 + height)], EDGE)
    tree_crown(s, -4, 26, 26, 23)
