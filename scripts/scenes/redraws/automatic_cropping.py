from geometry import BOLD
from scenes.redraws._w2 import chart_line, photo_print

DESCRIPTION = "Four bold crop corners frame the mountains and sun inside a landscape print."


def draw(s):
    point = photo_print(s)
    for x, z, dx, dz in ((17, 16, 1, 1), (92, 16, -1, 1),
                         (15, 69, 1, -1), (95, 69, -1, -1)):
        chart_line(s, point, [(x, z + 9*dz), (x, z), (x + 11*dx, z)], BOLD)
