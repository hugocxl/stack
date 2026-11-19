from geometry import DETAIL, EDGE
from scenes.redraws._w2 import face_arrow

DESCRIPTION = "A prefabricated room module slides into an open bay of a house frame."


def draw(s):
    s.box(-42, -24, 0, 84, 48, 5, 1)
    for x, y in ((-42, -24), (-3, -24), (38, -24), (-42, 20), (-3, 20)):
        s.box(x, y, 5, 4, 4, 39, .6)
    s.box(-42, -24, 41, 84, 4, 4, .6)
    for x in (-42, -3, 38):
        s.tube([(x + 2, -23, 45), (x + 2, 0, 59), (x + 2, 23, 45)], 1.55)
    s.tube([(-40, 0, 59), (40, 0, 59)], 1.5)
    s.box(-42, 20, 41, 84, 4, 4, .6)
    s.line([(4, 5, 5), (38, 5, 5)], DETAIL)

    s.box(5, 9, 5, 32, 34, 30, 1)
    s.box(4, 8, 35, 34, 36, 4, 1)
    window = [(10, 43.1, 12), (31, 43.1, 12), (31, 43.1, 28), (10, 43.1, 28)]
    s.face(window, EDGE)
    s.line([(20.5, 43.2, 12), (20.5, 43.2, 28)], DETAIL)
    face_arrow(s, lambda y, z: (37.1, y, z), [(37, 18), (17, 18)], EDGE, head=5.5)
