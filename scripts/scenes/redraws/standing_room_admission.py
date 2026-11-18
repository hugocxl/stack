from geometry import BOLD
from scenes.redraws._w3 import ticket

DESCRIPTION = "A perforated admission ticket shows two side-by-side shoeprints."


def draw(s):
    face = ticket(s)
    for x, v, direction in ((26, 24, -1), (51, 24, 1)):
        sole = [(-6, -5), (-7, 3), (-6, 10), (-3, 14), (2, 15),
                (6, 12), (7, 7), (6, 1), (4, -5)]
        def stamp(points, closed=False):
            face.stroke([(x + a + .19 * b * direction, v + b) for a, b in points],
                        BOLD, closed=closed)
        stamp(sole, closed=True)
        stamp([(-4, -9), (4, -9), (4, -15), (1, -17), (-4, -15)], closed=True)
        stamp([(-3, 7), (0, 8), (3, 7)])
