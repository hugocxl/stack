from geometry import EDGE
from scenes.redraws._w5 import lens_outline, parcel_mark, photo_print

DESCRIPTION = "Two overlapping parcel photos show the same box with a circle marking the broken seal in the front photo."


def draw(s):
    before = photo_print(s, -24, 8, 5, width=54, height=46)
    parcel_mark(s, before, 22, 24, .93)
    after = photo_print(s, 17, -5, width=54, height=46)
    parcel_mark(s, after, 27, 24, .93, broken=True)
    lens_outline(s, after, 34, 23, 8.5, EDGE)
