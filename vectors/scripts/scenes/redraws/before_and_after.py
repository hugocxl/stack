from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import Surface

DESCRIPTION = "A bold seam divides one house into a cracked half and a restored half."


def draw(s):
    s.face([(78, 0, 0), (78, 47, 0), (78, 47, 47), (78, 0, 47)])
    s.face([(0, 47, 0), (78, 47, 0), (78, 47, 46), (39, 47, 73),
            (0, 47, 46)])
    s.face([(39, -4, 76), (83, -4, 45), (83, 52, 45), (39, 52, 76)])
    s.face([(-5, -4, 45), (39, -4, 76), (39, 52, 76), (-5, 52, 45)])
    s.face([(-5, 52, 45), (39, 52, 76), (83, 52, 45), (78, 49, 43),
            (39, 49, 70), (0, 49, 43)], DETAIL)
    front = Surface(s, lambda u, v: (u, 47, v))
    for u in (9, 49):
        front.frame(u, 18, 19, 19, 1, EDGE)
    front.line([(58.5, 18), (58.5, 37)])
    front.line([(49, 27.5), (68, 27.5)])
    front.line([(19, 18), (23, 25), (19, 28), (22, 37)], EDGE)
    front.line([(1, 7), (10, 10), (14, 6), (20, 10), (25, 7)], EDGE)
    front.line([(3, 15), (10, 15), (10, 10)], DETAIL)
    front.line([(31, 46), (30, 41), (25, 42), (22, 38)], DETAIL)
    s.line([(63, 9, 59.1), (63, 47, 59.1)], DETAIL)
    s.line([(39, 52, 76), (39, 52, 71), (39, 47, 68), (39, 47, 0)], BOLD)
