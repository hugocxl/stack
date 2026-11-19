from geometry import DETAIL, EDGE
from scenes.redraws._w1 import tree_crown

DESCRIPTION = "A young tree takes root in a raised riverbank just above the waterline."


def draw(s):
    water = [(-41, -26), (34, -26), (45, -9), (45, 25),
             (35, 34), (-31, 34), (-42, 23)]
    s.solid(water, 0, 4)
    shore = [(-37, 13), (-21, 10), (-8, 4), (7, -4), (23, -6), (40, -12)]
    bank = [(-41, -26), (34, -26), (40, -13), *reversed(shore[:-1]),
            (-39, 13), (-42, 7)]
    s.face([(*p, 13) for p in bank], EDGE)
    bank_edge = [(*point, 13) for point in shore]
    water_edge = [(x, y + 3, 4) for x, y in reversed(shore)]
    s.face(bank_edge + water_edge, EDGE)
    s.ellipse(-7, -9, 13, 10.5, 6, DETAIL)
    tree_crown(s, -7, -9, 24, 20)
    for a, b in (((-22, 23), (3, 17)), ((3, 27), (30, 17)),
                 ((23, 8), (38, 3))):
        s.line([(*a, 4), ((a[0]+b[0])/2, (a[1]+b[1])/2+1.5, 4), (*b, 4)], DETAIL)
