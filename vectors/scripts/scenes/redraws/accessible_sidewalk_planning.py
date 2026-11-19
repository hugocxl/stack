from geometry import DETAIL, EDGE
from scenes.systems_shapes import rectangle

DESCRIPTION = "A wide curb ramp with a tactile paving strip connects a continuous sidewalk corner to a crossing."


def draw(s):
    roadbed = [(-46, -28), (43, -28), (43, 33), (31, 46),
               (-37, 46), (-46, 37)]
    s.solid(roadbed, -4, 4, crease=False)
    s.face([(43, -28, 0), (43, -28, 8), (43, 4, 8), (43, 4, 0)], EDGE)
    s.face([(43, 4, 0), (43, 4, 8), (37, 14, 8), (29, 20, 8),
            (15, 23, 8), (15, 25, 0), (29, 20, 0), (37, 14, 0)], EDGE)
    s.face([(-46, 23, 0), (-46, 23, 8), (-29, 23, 8), (-25, 25, 0)], EDGE)
    s.face([(-46, -28, 8), (43, -28, 8), (43, 4, 8), (37, 14, 8),
            (29, 20, 8), (15, 23, 8), (4, 6, 8), (-19, 6, 8), (-29, 23, 8),
            (-46, 23, 8)], EDGE)
    s.face([(-29, 23, 8), (-19, 6, 8), (4, 6, 8), (15, 23, 8),
            (15, 25, 0), (-25, 25, 0)], EDGE)
    s.line([(-22, 14, 4.65), (10, 14, 4.65)], DETAIL)
    for y, z in ((17, 3.4), (22, 1.7)):
        for x in (-18, -12, -6, 0, 6):
            s.ellipse(x, y, z, 1.55, 1.33, EDGE)
    s.line([(-31, -28, 8), (-31, -2, 8), (-36, 23, 8)], DETAIL)
    s.line([(-31, -2, 8), (43, -2, 8)], DETAIL)
    s.line([(22, -28, 8), (22, -2, 8), (32, 18, 8)], DETAIL)
    for x in (-18, -8, 2):
        rectangle(s, x, 29, 0, 5, 12, DETAIL, 1)
