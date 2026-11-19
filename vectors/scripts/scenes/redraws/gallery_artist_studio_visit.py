from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w3 import ticket

DESCRIPTION = "A notched admission ticket carries a large artist’s easel pictogram beside its perforated stub."


def draw(s):
    face = ticket(s, depth=4)
    at = face.viewer_axes(38, 24)

    def stroke(points, ink=EDGE, *, closed=False):
        face.stroke([at(x, y) for x, y in points], ink, closed=closed)

    stroke([(-9, -16), (-6, -7)])
    stroke([(6, -7), (9, -16)])
    stroke([(-2, 13), (0, 17), (2, 13)])
    stroke([(-12, -7), (12, -7)])
    stroke([(-11, -7), (-11, 13), (11, 13), (11, -7)], BOLD, closed=True)
    stroke([(-8, -3), (-3, 3), (1, 0), (5, 7), (8, 2)], DETAIL)
