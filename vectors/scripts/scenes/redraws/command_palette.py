from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import attached_panel, nav_path, product_laptop, search_control

DESCRIPTION = "A command palette floats above a laptop keyboard with one search field and one outlined command row."


def draw(s):
    screen = product_laptop(s)
    face = attached_panel(screen, 4)
    face.slab(rounded(2, 16, 79, 49, 4), 4)
    search_control(face, 9, 49, 65, 11, query=20)
    face.frame(8, 32, 67, 13, 2, BOLD)
    face.rows(13, 38, (26,), ink=EDGE)
    nav_path(face, [(66, 42), (66, 38), (57, 38)], head=3)
    face.rows(13, 24, (21,))
