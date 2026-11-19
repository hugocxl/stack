from geometry import EDGE, rounded
from scenes.redraws._w4 import paper

DESCRIPTION = "An e-reader shows a page of print above a progress rail with its marker partway across."


def draw(s):
    reader = paper(s, 95, pitch=.46, angle=-26, depth=7)
    reader.slab(rounded(0, 0, 76, 95, 5), 7)
    reader.frame(7, 7, 62, 70, 3, EDGE)
    reader.rows(15, 19, (35,), ink=EDGE)
    reader.rows(15, 30, (44, 42, 45, 40, 44, 31), step=6)
    reader.line([(47, 85), (65, 85)])
    reader.line([(12, 85), (37, 85)], EDGE)
    reader.oval(42, 85, 5, 5, EDGE)
