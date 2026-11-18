from geometry import DETAIL, EDGE
from scenes.redraws._w4 import desktop_display

DESCRIPTION = "A desktop browser dashboard displays a navigation sidebar and four distinct modules."


def draw(s):
    face = desktop_display(s, width=107, height=74, angle=-19)
    face.line([(5, 57), (102, 57)], EDGE)
    for u in (11, 16, 21):
        face.oval(u, 62, 1.2, 1.2, EDGE)
    face.line([(30, 6), (30, 57)], EDGE)
    face.rows(10, 47, (13, 9, 11, 7), step=-9)
    for u in (36, 69):
        for v in (11, 34):
            face.frame(u, v, 27, 18, 2)
    face.line([(41, 39), (46, 44), (51, 42), (58, 47)], EDGE)
    face.oval(82, 43, 6, 6, EDGE)
    face.line([(82, 49), (82, 43), (88, 43)], EDGE)
    for u, h in ((43, 5), (49, 9), (55, 12)):
        face.line([(u, 14), (u, 14 + h)], EDGE)
    face.rows(74, 23, (17, 12, 15), step=-4)
