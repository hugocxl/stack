from geometry import BOLD, GUIDE, rounded
from scenes.redraws._w3 import Surface, reader_page

DESCRIPTION = "A narrow reading ruler rests directly over one line of text on a folio."


def draw(s):
    page = reader_page(s)
    page.rules(11, 52, [52, 47], gap=9, ink=GUIDE)
    page.rules(11, 22, [50, 39], gap=8, ink=GUIDE)
    ruler = Surface(s, page.point(0, 0, -3), rise=page.rise, back=page.back)
    ruler.plate(rounded(-4, 26, 85, 13, 3), 3)
    ruler.rect(6, 29, 61, 7, 2)
    ruler.rules(12, 32.5, [47], ink=BOLD)
