from geometry import BOLD
from scenes.redraws._w4 import nav_phone, nav_result_rows, search_control

DESCRIPTION = "Four focus corners surround the middle hit on a handheld search results screen."


def draw(s):
    face = nav_phone(s)
    search_control(face, 9, 68, 48, 12, query=20)
    nav_result_rows(face, 13, 55, (26, 27, 22), step=18)
    for u, du in ((8, 1), (58, -1)):
        for v, dv in ((28, 1), (45, -1)):
            face.line([(u, v + dv*5), (u, v), (u + du*8, v)], BOLD)
