from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "A standing accordion map traces a walking route to a large leaf-shaped field observation marker."


def draw(s):
    def point(x, z):
        panel = min(int(x // 32), 2)
        fraction = (x - 32 * panel) / 32
        return x, 15 * (fraction if panel == 1 else 1 - fraction), z

    for x in (0, 32, 64):
        s.face([point(x + u, v) for u, v in ((0, 0), (32, 0), (32, 66), (0, 66))])
    for path in (((4, 53), (13, 57), (18, 46), (32, 50), (42, 45)),
                 ((4, 16), (15, 18), (28, 13), (32, 17), (44, 12), (55, 16)),
                 ((67, 18), (78, 14), (84, 26), (93, 26))):
        s.line([point(x, z) for x, z in path], DETAIL)
    route = [(8, 25), (20, 33), (32, 30), (45, 37), (54, 27),
             (64, 34), (69, 44)]
    s.line([point(x, z) for x, z in route], EDGE, dashed=True)
    Surface(s, point(*route[0])).oval(0, 0, 2.8, 2.8, EDGE)
    leaf = [(67, 42), (68, 51), (75, 58), (89, 63), (88, 53),
            (83, 45), (76, 42)]
    s.face([point(x, v) for x, v in leaf], BOLD)
    s.line([point(x, v) for x, v in ((67, 42), (76, 48), (82, 54))], EDGE)
