from math import asin, degrees

from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w3 import loop, upright

DESCRIPTION = "A coin slips into the slot of a donation box marked with a heart."


def draw(s):
    left, right, back, front, top = -34, 34, -24, 24, 31
    slot_x, slot_y = 5, 10
    slot_half_depth = 5
    lip = slot_y + slot_half_depth
    slot = rounded(slot_x - 21, slot_y - slot_half_depth, 42, 2 * slot_half_depth, 3)

    s.face([(left, back, top), (right, back, top),
            (right, front, top), (left, front, top)],
           openings=[[(x, y, top) for x, y in slot]])
    s.face([(right, back, 0), (right, front, 0), (right, front, top),
            (right, back, top)])
    s.face([(left, front, 0), (right, front, 0), (right, front, top),
            (left, front, top)])

    loop(s, [(-6, 9), (-9, 12), (-11, 16), (-10.5, 19), (-8, 21),
             (-5, 21.5), (-2, 20), (0, 17.5), (2, 20), (5, 21.5),
             (8, 21), (10.5, 19), (11, 16), (9, 12), (6, 9), (0, 4)],
         EDGE, y=front)

    # These chords project onto the near lip, where the coin disappears.
    center, radius = 39.5, 17
    for y, ink in ((slot_y - 2.5, EDGE), (slot_y, BOLD)):
        cutoff = top + y - lip
        angle = degrees(asin((cutoff - center) / radius))
        s.face(upright(oval(slot_x, center, radius, radius, angle, 180 - angle), y), ink)
    loop(s, oval(slot_x, center, 11.5, 11.5, count=48)[:-1], DETAIL, y=slot_y)
