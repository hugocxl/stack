from geometry import EDGE
from scenes.commerce_objects import pallet

DESCRIPTION = "A loaded shipping pallet sits squarely within four painted floor bay corners."


def draw(s):
    for x, y, dx, dy in ((-37, -35, 1, 1), (37, -35, -1, 1),
                         (37, 35, -1, -1), (-37, 35, 1, -1)):
        s.line([(x + dx * 15, y, 0), (x, y, 0), (x, y + dy * 15, 0)], EDGE)
    pallet(s)
