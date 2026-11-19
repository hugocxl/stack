from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import chart_marker, level_face

DESCRIPTION = "Three incoming routes merge into one arrow that leads to a shopping bag."


def draw(s):
    for z, route in ((74, [(17, 74), (35, 74), (55, 50)]),
                     (50, [(17, 50), (55, 50)]),
                     (26, [(17, 26), (35, 26), (55, 50)])):
        chart_marker(s, level_face, 11, z, 6)
        s.line([level_face(*p) for p in route], EDGE)
    arrow(s, [level_face(55, 50), level_face(76, 50)], BOLD, head=7)
    s.box(46, -49, 18, 32, 17, 43, 2)
    s.tube([(54, -32, 51), (54, -32, 63), (57, -32, 70),
            (64, -32, 73), (71, -32, 69), (73, -32, 63),
            (73, -32, 51)], 1.2, EDGE)
