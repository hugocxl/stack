from geometry import DETAIL
from scenes.redraws._w5 import crop_furrow

DESCRIPTION = "A crop row has a compact monitoring sensor mounted on a stake at canopy height."


def draw(s):
    crop_furrow(s)
    s.tube([(62, 9, 4), (62, 9, 25)], 1.2)
    s.box(58, 5, 24, 10, 8, 9, 1.5)
    s.disk(62, 9, 33, 1.6, 1.6, 3)
    for z in (27, 30):
        s.line([(60, 13, z), (66, 13, z)], DETAIL)
