from geometry import EDGE
from scenes.redraws.page_moved import Surface

DESCRIPTION = "An upright folder is outlined with dashes and has an outward share arrow in its raised tab."


def draw(s):
    back = Surface(s, (8, 4, 4), side=True, lean=.15)
    back.loop([(0, 0), (105, 0), (105, 51), (68, 51), (61, 65),
               (13, 65), (6, 51), (0, 51)], EDGE, dashed=True)
    front = Surface(s, (14, 4, 0), side=True, lean=-.10)
    front.loop([(0, 0), (105, 0), (105, 39), (102, 42),
                (3, 42), (0, 39)], EDGE, dashed=True)
    back.arrow([(26, 48), (26, 51), (30, 55), (50, 55)], EDGE, head=7)
