from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import front_surface
from scenes.redraws.saved_filter_preset import bookmark

DESCRIPTION = "A search field has an inset magnifying glass and a folded bookmark ribbon on its right edge."


def draw(s):
    search = front_surface(s, angle=8, z=8, lean=.24)
    search.slab(rounded(0, 0, 106, 41, 12), 8)
    search.frame(6, 7, 94, 27, 8, EDGE)
    search.oval(22, 22, 6, 6, BOLD)
    search.line([(26, 18), (31, 13)], BOLD)
    search.line([(40, 12), (40, 29)], EDGE)
    bookmark(search, 79, 44)
