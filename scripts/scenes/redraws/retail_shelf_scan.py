from geometry import BOLD, EDGE
from scenes.redraws._w1 import barcode, stock_shelf

DESCRIPTION = "Scan brackets frame a barcode label on the front of a stocked shelf."


def draw(s):
    stock_shelf(s)
    y = 24
    s.box(-21, 19, 19, 44, 5, 20, 1.3)
    barcode(s, -15, y, 23, 32, 12)
    for x, dx in ((-19, 1), (21, -1)):
        for z, dz in ((21, 1), (37, -1)):
            s.line([(x + dx * 5, y, z), (x, y, z), (x, y, z + dz * 4)], BOLD)
