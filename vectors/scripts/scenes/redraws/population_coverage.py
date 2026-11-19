from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import profile_mark

DESCRIPTION = "A partly unfolded map outlines a service area around three customer markers."


def draw(s):
    folds = [(0, 6), (28, -11), (95, 7), (119, -11)]

    def p(x, z):
        for (a, b), (c, d) in zip(folds, folds[1:]):
            if a <= x <= c:
                return x, b + (x - a)*(d - b)/(c - a) - z*.11, z
        raise ValueError(x)

    for (a, _), (b, _) in zip(folds, folds[1:]):
        s.face([p(a, 0), p(b, 0), p(b, 80), p(a, 80)], EDGE)
    for road in ([(2, 20), (17, 25), (28, 30), (44, 33), (62, 25), (81, 28), (95, 26), (117, 18)],
                 [(3, 57), (14, 48), (28, 51), (41, 63), (55, 70), (72, 64), (95, 62), (117, 69)],
                 [(19, 4), (18, 15), (22, 38), (15, 55), (19, 68), (17, 77)],
                 [(109, 3), (110, 15), (102, 33), (107, 50), (105, 76)]):
        s.line([p(x, z) for x, z in road], DETAIL)
    perimeter = [(37, 23), (39, 52), (52, 64), (75, 63), (90, 50),
                 (88, 26), (75, 18), (53, 20), (37, 23)]
    s.line([p(x, z) for x, z in perimeter], BOLD)
    for x, z in ((52, 40), (76, 41), (64, 54)):
        profile_mark(s, p, x, z, 10, EDGE)
