from geometry import EDGE, rounded
from scenes.redraws._w4 import media_frame, paper

DESCRIPTION = "A video timeline places a short advertisement clip directly beyond the end marker of the main clip."


def draw(s):
    page = paper(s, 64, pitch=.59, angle=-13, depth=5)
    page.slab(rounded(0, 0, 128, 64, 4), 5)
    page.rows(8, 13, (112,), ink=EDGE)
    for u in range(10, 120, 10):
        page.line([(u, 13), (u, 18)])
    media_frame(page, 9, 27, 69, 27)
    page.frame(84, 27, 35, 27, 2, EDGE)
    page.outline([(88, 38), (96, 38), (109, 32), (109, 49), (96, 44), (88, 44)], EDGE)
    page.line([(96, 44), (100, 51)], EDGE)
    page.line([(81, 19), (81, 57)], EDGE)
    page.outline([(77, 16), (85, 16), (81, 21)], EDGE)
