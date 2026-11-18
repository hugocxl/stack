from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._w5 import currency_mark, printed_stroke, ruled_amounts

DESCRIPTION = "A curled receipt shows three separately aligned fee amounts above a total rule."


def draw(s):
    face = lambda x, z: (x, -.32 * z, z)
    outline = [(0, 10), (49, 10), (49, 66), (44, 62), (39, 66), (34, 62),
               (29, 66), (24, 62), (19, 66), (14, 62), (9, 66), (4, 62), (0, 66)]
    s.face([face(x, z) for x, z in outline], EDGE)
    printed_stroke(s, face, [(8, 53), (29, 53)], EDGE)
    ruled_amounts(s, face, ((43, 14), (35, 19), (27, 11)), 7, 43, width=11)
    printed_stroke(s, face, [(7, 21), (43, 21)], EDGE)
    currency_mark(s, face, 26, 15, 3.6)
    printed_stroke(s, face, [(33, 15), (43, 15)], EDGE)

    curl = oval(2, 6.3, 6.5, 6.3, count=36)
    roll = MultiPoint([project((x, y, z)) for x in (0, 49) for y, z in curl]).convex_hull
    s.layers.append((roll.boundary, roll, EDGE))
    s.line([(49, y, z) for y, z in curl], EDGE)
    s.line([(49, y, z) for y, z in oval(2, 6.3, 4, 3.7, 45, 312, 22)], DETAIL)
