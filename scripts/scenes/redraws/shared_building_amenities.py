from geometry import DETAIL, EDGE

DESCRIPTION = "An apartment building opens at ground level to show a shared lounge with a sofa and low coffee table."


def draw(s):
    s.box(0, 0, 0, 78, 40, 5, 1)
    s.box(0, 0, 5, 78, 9, 49, 1)
    s.box(0, 9, 5, 5, 31, 49, 1)
    s.box(72, 9, 5, 6, 31, 49, 1)

    # Seat, backrest and arms form one lounge sofa.
    s.box(9, 22, 6, 41, 13, 8, 2)
    s.box(9, 20, 10, 41, 4, 12, 2)
    for x in (9, 46):
        s.box(x, 23, 12, 4, 12, 7, 1)
    s.line([(30, 24, 14), (30, 34, 14)], DETAIL)
    s.disk(57, 32, 5, 5, 3.4, 4)
    s.disk(57, 32, 9, 12, 7, 2)

    s.box(0, 0, 52, 78, 40, 52, 1)
    for z in (61, 81):
        for x in (9, 30, 51):
            s.box(x, 40, z, 12, 1.4, 14, 1)
        s.line([(78, 12, z), (78, 24, z), (78, 24, z + 13), (78, 12, z + 13),
                (78, 12, z)], DETAIL)
    s.box(-2, -2, 103, 82, 44, 4, 1)
