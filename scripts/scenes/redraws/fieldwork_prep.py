from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_check

DESCRIPTION = "A hiking pack carries a field checklist tag with a mountain trail and three checked equipment rows."


def draw(s):
    for x in (14, 44):
        s.tube([(x, -2, 52), (x, -11, 42), (x, -14, 29), (x, -3, 15)], 2.7)
    s.tube([(21, 7, 68), (22, 6, 76), (27, 6, 79), (36, 6, 79),
            (41, 6, 76), (42, 7, 68)], 2.2)
    pack = Surface(s, (0, 26, 0))
    pack.plate([(5, 0), (57, 0), (63, 5), (65, 45), (62, 58), (54, 66),
                (42, 70), (22, 70), (10, 66), (4, 57), (1, 43), (0, 7)], 26)
    pack.stroke([(6, 45), (10, 54), (19, 59), (31, 61),
                 (44, 60), (54, 56), (59, 49)], EDGE)
    pack.stroke([(12, 53), (14, 47)], EDGE)
    pouch = Surface(s, (0, 29, 0))
    pouch.plate(rounded(8, 6, 44, 27, 6), 4)
    pouch.rules(13, 24, [33], ink=EDGE)
    pouch.stroke([(17, 24), (17, 18)], EDGE)

    s.tube([(56, 26, 55), (59, 30, 65), (66, 32, 69), (72, 31, 66)], 1.3)
    tag = Surface(s, (51, 34, 6), rise=(-.08, .99), back=(0, -1, -.08))
    tag.plate([(0, 0), (55, 0), (55, 49), (44, 60), (13, 60), (0, 49)], 3)
    tag.oval(21, 54, 2.7, 2.7, EDGE)
    s.tube([(72, 31, 66), (74, 30.5, 63), tag.point(21, 55)], 1.15)
    tag.stroke([(8, 34), (20, 46), (29, 37), (36, 44), (47, 34)], BOLD)
    tag.stroke([(12, 29), (26, 30), (25, 35), (35, 36)], DETAIL, dashed=True)
    for v, width in ((23, 21), (15, 16), (7, 19)):
        tag.rules(10, v, [width], ink=EDGE)
        printed_check(tag, 43, v, 4.3)
