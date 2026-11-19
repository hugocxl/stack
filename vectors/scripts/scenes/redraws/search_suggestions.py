from geometry import EDGE
from scenes.redraws._w4 import nav_phone, search_control, search_mark

DESCRIPTION = "Three suggested query rows drop directly below the search field on a handheld screen."


def draw(s):
    face = nav_phone(s, width=72, height=89, angle=-19)
    search_control(face, 9, 60, 54, 13, query=23)
    face.frame(10, 12, 52, 48, 3, EDGE)
    for i, (v, width) in enumerate(((52, 33), (36, 26), (20, 31))):
        search_mark(face, 17, v + 1, 2.5)
        face.rows(25, v, (width,), ink=EDGE)
        if i < 2:
            face.line([(12, v - 8), (60, v - 8)])
