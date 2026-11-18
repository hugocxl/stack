from geometry import DETAIL, EDGE, oval

DESCRIPTION = "An open-jaw wrench grips the lower service valve on a wall-mounted radiator."


def draw(s):
    s.box(-38, -12, 0, 76, 12, 64, 1)
    for z in (21, 46):
        s.tube([(-32, 5, z), (28, 5, z)], 3.2, EDGE)
    for x in (-30, -20, -10, 0, 10, 20):
        s.box(x, 2, 16, 7, 10, 36, 3)
    s.tube([(26, 7, 21), (34, 7, 21), (34, 7, 7), (34, 2, 7)], 2.5)
    s.box(30, 4, 16, 8, 7, 7, 1)

    def tool(u, v):
        return 34 + .64*u, 14 - .36*u, 20 + v

    outline = [(-9, -3), (-11, 4), (-8, 9), (-6, 5), (-4, 0),
               (2, 0), (4, 6), (6, 3), (6, -3), (3, -9), (23, -22),
               (22, -26), (17, -27), (-3, -11)]
    s.face([tool(u, v) for u, v in outline], EDGE)
    s.line([tool(2, -11), tool(19, -23)], DETAIL)
    s.line([tool(u, v) for u, v in oval(19, -24, 1.0, .85, count=18)], DETAIL)
