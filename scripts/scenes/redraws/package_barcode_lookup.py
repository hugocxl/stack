from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w1 import barcode, software_package

DESCRIPTION = "A magnifying glass frames the bold barcode label on a shipping carton."


def draw(s):
    software_package(s, 0, 0, 0, 1.26, show_code=False)
    barcode(s, -28, 26.46, 11, 48, 23)

    x, y, z = 4, 30, 25
    outer = oval(x, z, 24, 22, count=48)[:-1]
    inner = oval(x, z, 20.8, 18.8, count=48)[:-1]
    s.tube([(x + 18, y, z - 14), (x + 33, y, z - 28)], 3, EDGE)
    s.face([(a, y + .8, b) for a, b in outer], BOLD,
           openings=([(a, y + .8, b) for a, b in inner],))
    s.line([(a, y, b + 1.7) for a, b in oval(x, z, 24, 22, 8, 162, count=24)], DETAIL)
