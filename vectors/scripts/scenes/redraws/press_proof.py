from geometry import DETAIL, EDGE
from scenes.redraws._w4 import landscape, magnifier, proof_page

DESCRIPTION = "A printed proof shows crop marks around its layout and a magnifier over the typeset copy."


def draw(s):
    page = proof_page(s, crop=True)
    landscape(page, 15, 38, 26, 31)
    page.rows(47, 41, (18, 19, 17, 18, 13), step=6)
    page.rows(15, 76, (48, 40), step=7)
    magnifier(page, 65, 57, 16, text=((-4, 15, EDGE), (3, 19, DETAIL)))
