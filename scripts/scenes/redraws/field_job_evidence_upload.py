from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import photo_print

DESCRIPTION = "A job-site photograph shows a repaired pipe joint with an upload badge on the print's corner."


def draw(s):
    photo = photo_print(s, 99, 82, angle=-14, image=False)
    photo.frame(7, 6, 85, 59, 2)
    photo.line([(8, 19), (61, 19)], DETAIL)
    photo.line([(23, 7), (23, 19)], DETAIL)
    photo.line([(8, 55), (73, 55)], DETAIL)
    photo.line([(25, 55), (25, 64)], DETAIL)
    photo.line([(8, 29), (33, 29), (36, 30.5)], EDGE)
    photo.line([(8, 44), (36, 44)], EDGE)
    photo.line([(55, 31), (64, 31), (67, 27), (67, 22)], EDGE)
    photo.line([(55, 46), (70, 46), (79, 42), (82, 35), (82, 22)], EDGE)
    for u in (67, 82):
        photo.line([(u, 16), (u, 7)], EDGE)
    photo.frame(36, 25, 19, 25, 4, EDGE)
    photo.line([(42, 26), (42, 49)], DETAIL)
    photo.line([(49, 26), (49, 49)], DETAIL)
    photo.oval(45.5, 30, 1, 1, EDGE)
    photo.oval(45.5, 44, 1, 1, EDGE)
    photo.frame(64, 16, 21, 6, 1, EDGE)
    badge(s, "up", *photo.at(94, 52), 14)
