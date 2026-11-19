from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import desk_calendar

DESCRIPTION = "A standing ring-bound calendar has an empty grid with one dashed appointment slot in the middle."


def draw(s):
    face = desk_calendar(s, 81, 76)
    for x in (25, 55):
        face.stroke([(x, 8), (x, 42)], DETAIL)
    for z in (8, 19, 31, 42):
        face.rules(8, z, [65], ink=DETAIL)
    face.stroke(rounded(28, 21, 24, 8, 1), EDGE, closed=True, dashed=True)
