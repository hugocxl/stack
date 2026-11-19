from geometry import DETAIL, EDGE
from scenes.redraws._w3 import flat, theater_seat, wheelchair

DESCRIPTION = "Two theater seats share a reserved row with an outlined wheelchair bay."


def draw(s):
    bay = flat(s, 88, 47, 0)
    bay.rect(2, 1, 49, 43, 4, EDGE)
    wheelchair(bay, 27, 22, 27)
    s.line([(5, 46, 0), (88, 46, 0)], DETAIL)
    theater_seat(s, 0)
    theater_seat(s, 45)
