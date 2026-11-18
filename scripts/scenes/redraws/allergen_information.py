from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.systems_shapes import bezel

DESCRIPTION = "A warning triangle overlaps the upper edge of a gable-top food carton’s ingredient label."


def draw(s):
    # The ridge runs parallel to the ingredient label. The near roof slope
    # and right gable meet the folded strip along the top.
    s.face([(0, 0, 49), (0, 16, 63), (50, 16, 63), (50, 0, 49)])
    s.face([(0, 16, 63), (50, 16, 63), (50, 16, 68), (0, 16, 68)])
    s.face([(0, 16, 63), (0, 32, 49), (50, 32, 49), (50, 16, 63)])
    s.face([(50, 0, 49), (50, 16, 63), (50, 32, 49)])
    s.face([(50, 0, 0), (50, 32, 0), (50, 32, 49), (50, 0, 49)])
    s.face([(0, 32, 0), (50, 32, 0), (50, 32, 49), (0, 32, 49)])

    bezel(s, 7, 32, 6, 36, 34, EDGE, 1)
    s.line([(7, 32, 30), (43, 32, 30)], EDGE)
    s.line([(12, 32, 35), (26, 32, 35)], DETAIL)
    for z, width in ((24, 22), (19, 25), (14, 18)):
        s.line([(12, 32, z), (12 + width, 32, z)], DETAIL)

    warning(s, 46, 36, 34, 29)
