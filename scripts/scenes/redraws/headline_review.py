from geometry import BOLD, EDGE
from scenes.redraws._w4 import magnifier, proof_page

DESCRIPTION = "A magnifier enlarges the middle of a proof’s headline above two columns of article text."


def draw(s):
    page = proof_page(s)
    page.rows(12, 52, (25, 23, 26, 20, 23, 16), step=6)
    page.rows(46, 52, (23, 19, 23, 24, 19, 15), step=6)
    page.rows(66, 20, (8,), ink=BOLD)
    magnifier(page, 41, 23, 16.5, text=((-2, 23, BOLD), (6, 18, EDGE)))
