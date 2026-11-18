from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import proof_page

DESCRIPTION = "A typeset proof carries an insertion caret and a strike-through directly across its copy."


def draw(s):
    page = proof_page(s)
    page.rows(13, 42, (52,), ink=EDGE)
    page.rows(13, 51, (54, 47, 49), step=15, ink=DETAIL)
    page.rows(12, 87, (39,), ink=DETAIL)
    page.line([(26, 65), (34, 51), (42, 65)], BOLD)
    for u, width in ((23, 6), (33, 11), (48, 8), (60, 5)):
        page.rows(u, 74, (width,), ink=DETAIL)
    page.line([(20, 76), (39, 74), (53, 76), (67, 74)], BOLD)
