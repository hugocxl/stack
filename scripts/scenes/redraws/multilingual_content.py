from geometry import EDGE, rounded
from scenes.redraws._w4 import Surface, paper

DESCRIPTION = "Two overlapping translation cards pair left-aligned rows with right-aligned cursive strokes."


def draw(s):
    frame = paper(s, 73, pitch=.88, run=.35, angle=-26, depth=6)
    frame.slab(rounded(0, 0, 69, 58, 6), 4)
    top = Surface(s, lambda u, v: frame.at(u + 65, v + 14))
    top.slab(rounded(0, 0, 70, 58, 6), 6)

    frame.rows(10, 16, (43, 30, 40, 24), step=9, ink=EDGE)
    for v, w in ((16, 31), (25, 46), (34, 28), (43, 41)):
        top.line([(60 - w, v + 1), (63 - w, v + 3), (68 - w, v + 3),
                  (73 - w, v), (76 - w, v + 3), (52, v + 3), (56, v + 1), (60, v - 3)], EDGE)
        top.rows(47, v - 1, (1.8,))
