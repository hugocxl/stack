from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import front_marks, outline, search_display, section

DESCRIPTION = "A search display shows one result with a star rating beside its title."


def draw(s):
    p = search_display(s, 125, 77)
    outline(s, 11, 0, 45, 103, 12, 6, EDGE)
    front_marks(s, 21, 0, 51, "search", .74)
    section(s, p, 34, 51, (30,))
    section(s, p, 11, 29, (35, 46, 39))
    for i in range(4):
        glyph(s, "star", 69 + i*14, 0, 30, 8, BOLD if i < 3 else DETAIL)
