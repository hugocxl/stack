from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open museum booklet pairs a printed illustration of a two-handled amphora with short lesson notes."


def draw(s):
    art, notes = open_book(s)

    def illustration(points):
        # Rotate the print across the page so the vessel reads upright in the view.
        return [(34 + .59 * (u + v), 35 + .59 * (v - u)) for u, v in points]

    art.outline(illustration([(-8, -24), (8, -24), (8, -20), (5, -19),
                              (5, -12), (12, -7), (15, -1), (15, 6),
                              (12, 12), (8, 16), (4, 19), (4, 22),
                              (8, 23), (8, 26), (-8, 26), (-8, 23),
                              (-4, 22), (-4, 19), (-8, 16), (-12, 12),
                              (-15, 6), (-15, -1), (-12, -7), (-5, -12),
                              (-5, -19), (-8, -20)]), BOLD)
    for side in (-1, 1):
        art.line(illustration([(side * u, v) for u, v in
                              ((5, -16), (13, -17), (18, -13), (19, -8),
                               (17, -4), (14, -2))]), EDGE)
    art.line(illustration([(-15, 3), (15, 3)]), DETAIL)
    notes.rows(75, 18, (36,), ink=EDGE)
    notes.rows(75, 30, (31, 36, 29, 17), step=8)
