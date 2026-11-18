from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A single card maps the Cyrillic letter Д to its Latin counterpart D with an arrow."


def draw(s):
    card = Surface(s, (0, 0, 0), rise=(-.46, .89), back=(0, -.89, -.46))
    card.plate(rounded(0, 0, 112, 53, 6), 11)
    for x in (7, 77):
        card.rect(x, 9, 28, 35, 3, EDGE)
    for x, letter in ((21, "cyrillic"), (91, "latin")):
        place = card.viewer_axes(x, 27)
        if letter == "cyrillic":
            paths = [[(-8, -11), (-8, -6), (8, -6), (8, -11)],
                     [(-5, -6), (-2, -1), (-1, 8), (5, 8), (5, -6)]]
        else:
            paths = [[(-6, -8), (-6, 8), (0, 8), (5, 6), (7, 2), (7, -2),
                      (5, -6), (0, -8), (-6, -8)]]
        for path in paths:
            card.stroke([place(a, b) for a, b in path], BOLD)
    printed_glyph(card, "arrow", 56, 26, 14, EDGE)
