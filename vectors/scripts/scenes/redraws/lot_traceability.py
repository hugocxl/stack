from geometry import DETAIL, EDGE
from scenes.redraws._w1 import barcode, price_tag, software_package

DESCRIPTION = "A large traceability tag with a lot barcode hangs from the taped seam of a shipping carton."


def draw(s):
    software_package(s, 0, 0, 0, 1.16, show_code=False)
    x, y, z = -13, 27, 9
    eye = price_tag(s, x, y, z, 37, length=1.13)
    s.line([(0, 16, 41.76), (0, 22.7, 41.76), (-.6, 25, 40),
            (-3, 27, 31), eye], EDGE)
    barcode(s, -2, y, 12, 27, 10)
    s.line([(0, y, 25), (23, y, 25)], DETAIL)
