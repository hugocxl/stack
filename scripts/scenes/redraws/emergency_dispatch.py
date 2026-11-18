from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import side_wheel, upright

DESCRIPTION = "A response van with a roof beacon points toward a forward dispatch arrow at road level."


def draw(s):
    for x in (22, 84):
        side_wheel(s, x, -22, 11, 10)

    profile = [(0, 15), (0, 51), (4, 60), (68, 60), (79, 55),
               (90, 36), (103, 32), (107, 27), (107, 15)]
    upright(s, profile, 24, 48)
    s.line([(4, 24, 60), (4, -24, 60), (68, -24, 60)], DETAIL)
    s.face([(77, -22, 54), (89, -22, 36), (89, 22, 36), (77, 22, 54)], EDGE)
    s.face([(73, 24, 52), (78, 24, 50), (87, 24, 35), (73, 24, 35)], EDGE)
    s.line([(94, 24, 30), (94, 24, 16)], DETAIL)
    s.line([(69, 24, 28), (75, 24, 28)], DETAIL)
    s.line([(10, 24, 40), (56, 24, 40)], EDGE)
    s.line([(10, 24, 33), (56, 24, 33)], DETAIL)
    s.face([(107, -24, 16), (107, 24, 16), (107, 24, 26), (107, -24, 26)], EDGE)
    for y in (-20, 13):
        s.line([(107, y, 23), (107, y + 7, 23)], EDGE)
    for x in (22, 84):
        side_wheel(s, x, 25, 11, 11)
    s.box(45, -15, 60, 14, 30, 4, 3)
    s.box(47, -13, 64, 10, 26, 5, 4)
    for y in (-7, 7):
        s.line([(48.5, y, 69), (55.5, y, 69)], DETAIL)
    s.line([(56, 2, 74), (56, 2, 78)], EDGE)
    s.line([(56, 9, 73), (56, 12, 77)], EDGE)
    arrow(s, [(106, -7, 1), (139, -7, 1)], BOLD, head=11)
