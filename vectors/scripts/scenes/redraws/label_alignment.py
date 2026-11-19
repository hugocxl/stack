from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import software_package
from scenes.systems_shapes import rectangle

DESCRIPTION = "A shipping label sits squarely inside four printed corner guides on a taped carton."


def draw(s):
    software_package(s, 0, 0, 0, 1.20, show_code=False)
    z = 43.2
    rectangle(s, 11, -14, z, 19, 28, EDGE, 1)
    for x, y, dx, dy in ((7.5, -18, 1, 1), (33.5, -18, -1, 1), (33.5, 18, -1, -1), (7.5, 18, 1, -1)):
        s.line([(x + dx * 5.5, y, z), (x, y, z), (x, y + dy * 5.5, z)], BOLD)

    for i, x in enumerate((14, 16, 18.5, 20, 23, 25, 27)):
        s.line([(x, 2, z), (x, 12, z)], EDGE if i % 2 == 0 else DETAIL)
    for y, length in ((-10, 10), (-6, 13)):
        s.line([(14, y, z), (14 + length, y, z)], DETAIL)
