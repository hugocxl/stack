from geometry import EDGE
from scenes.redraws._w4 import photo_print

DESCRIPTION = "A bordered photographic print shows a ring sculpture on a museum plinth."


def draw(s):
    print_ = photo_print(s, 96, 88, angle=15, image=False)
    print_.frame(7, 7, 82, 64, 2, EDGE)
    print_.outline([(29, 51), (56, 51), (67, 56), (67, 62), (37, 62), (29, 57)], EDGE)
    print_.line([(29, 51), (37, 56), (67, 56)], EDGE)
    print_.line([(37, 56), (37, 62)], EDGE)
    sculpture = [
        (35, 49), (29, 42), (27, 34), (28, 26), (33, 19), (40, 15),
        (48, 14), (57, 17), (64, 23), (68, 31), (67, 39), (64, 46),
        (58, 51), (50, 54), (42, 53),
    ]
    opening = [(40, 43), (36, 38), (36, 31), (39, 25), (45, 22), (52, 22),
               (58, 26), (61, 32), (59, 39), (55, 44), (48, 46)]
    s.face([print_.at(*p) for p in sculpture], EDGE,
           openings=([print_.at(*p) for p in opening],))
    print_.line([(36, 43), (32, 36), (33, 29), (38, 22), (46, 19),
                 (54, 19), (60, 22)])
