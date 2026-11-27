from geometry import DETAIL, EDGE
from scenes.redraws._sf import map_pin

DESCRIPTION = "A parcel follows a dashed route on the ground toward a standing map pin."


def draw(s):
    route = [(-58, 40, 0), (-30, 40, 0), (-14, 22, 0), (8, 6, 0), (30, 0, 0)]
    s.line(route, DETAIL, dashed=True)
    s.box(-82, 26, 0, 30, 28, 22, 2)
    for y in (36, 44):
        s.line([(-82, y, 22), (-52, y, 22), (-52, y, 16)], DETAIL)
    s.disk(30, 0, 0, 7, 7, 1.4)
    map_pin(s, 30, 0, 1, 18)
