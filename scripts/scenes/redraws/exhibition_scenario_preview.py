from geometry import EDGE, GUIDE
from scenes.redraws.sculpture_360_view import ring_sculpture

DESCRIPTION = "An open gallery display contains a ring sculpture and a dashed outline for the planned exhibit area."


def draw(s):
    s.box(0, 0, 0, 89, 53, 6, 2)
    s.box(0, 0, 6, 89, 4, 79, 1)
    s.box(85, 4, 6, 4, 49, 79, 1)

    outline = [(15, 5, 15), (73, 5, 15), (73, 5, 66), (15, 5, 66), (15, 5, 15)]
    s.line(outline, GUIDE, dashed=True)
    floor = [(15, 7, 6), (15, 43, 6), (73, 43, 6), (73, 7, 6)]
    s.line(floor, EDGE, dashed=True)
    ring_sculpture(s, 47, 31, 6, scale=.82)
    s.box(0, 0, 85, 89, 53, 5, 2)
