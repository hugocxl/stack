from geometry import EDGE
from scenes.redraws._w3 import browser_window

DESCRIPTION = "A file picker shows a single dashed file silhouette inside an otherwise empty list beside an inset search field."


def draw(s):
    picker = browser_window(s, 105, 78)
    picker.stroke([(0, 49), (105, 49)], EDGE)
    picker.rect(8, 53, 14, 6, 1)
    picker.rect(67, 52, 30, 8, 2)
    picker.oval(73, 57, 2, 2)
    picker.stroke([(74.3, 55.6), (76, 54)])
    picker.stroke([(0, 13), (105, 13)])
    picker.rect(76, 4, 21, 5, 1)
    ghost = [(39, 18), (65, 18), (65, 37), (58, 44), (39, 44)]
    picker.stroke(ghost, EDGE, closed=True, dashed=True)
    picker.stroke([(58, 44), (58, 37), (65, 37)], EDGE, dashed=True)
