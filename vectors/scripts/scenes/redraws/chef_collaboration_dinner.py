from geometry import DETAIL, EDGE
from scenes.redraws._w5 import printed_stroke

DESCRIPTION = "A plated dinner sits beside a standing menu with two chef hats printed side by side."


def draw(s):
    s.face([(28, 1, 0), (67, 1, 0), (67, 7, 33), (28, 7, 33)])
    face = lambda x, z: (x, 14 - 7 * z / 33, z)
    s.face([face(28, 0), face(67, 0), face(67, 33), face(28, 33)])
    for x in (39, 56):
        hat = [(-4, -5), (4, -5), (4, -1), (7, 1), (7, 4), (5, 6),
               (3, 6), (1, 9), (-2, 9), (-4, 6), (-6, 6), (-8, 3),
               (-7, 0), (-4, -1), (-4, -5)]
        printed_stroke(s, face, [(x + u*.86, 20 + v*.86) for u,v in hat], EDGE)
    s.disk(24, 34, 0, 23, 20, 3)
    s.ellipse(24, 34, 3, 18.5, 15)
    entree = [(10, 34), (12, 30), (19, 29), (23, 30), (25, 33),
              (31, 35), (30, 39), (26, 42), (17, 42), (12, 39)]
    s.solid(entree, 3, 4, crease=False)
    s.line([(15, 34, 7), (19, 32, 7), (22, 33, 7), (26, 37, 7)], DETAIL)
    for x, y in ((30, 26), (35, 29), (36, 34)):
        s.disk(x, y, 3, 2.8, 2.2, 2.2)
