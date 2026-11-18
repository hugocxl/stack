from geometry import BOLD, EDGE
from scenes.redraws._w4 import paper
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A folded-corner screening form shows a medical cross, short check rows, and a signed consent line."


def draw(s):
    page = paper(s, 96, pitch=.69, run=.69, angle=-20, depth=6)
    page.slab([(0, 0), (62, 0), (78, 16), (78, 96), (0, 96)], 6)
    page.line([(62, 0), (62, 16), (78, 16)], EDGE)
    medical_cross(page, 16, 17, 10, EDGE)
    page.rows(34, 14, (20, 14), step=7)
    for v in (39, 51):
        page.frame(10, v, 5, 5, .7, EDGE)
        page.rows(21, v + 2.5, (41,))
    page.line([(12, 83), (66, 83)], EDGE)
    page.line([(16, 80), (25, 70), (28, 67), (27, 64), (23, 66), (21, 74),
               (25, 78), (34, 72), (36, 77), (45, 70), (47, 76), (59, 73)], BOLD)
