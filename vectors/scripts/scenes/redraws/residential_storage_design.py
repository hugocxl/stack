from geometry import DETAIL, EDGE

DESCRIPTION = "An open built-in closet shows a clothes rail beside fitted shelves and a stack of drawers."


def draw(s):
    s.box(0, 0, 0, 82, 37, 6, 1)
    s.box(0, 0, 6, 82, 6, 82, 1)
    s.box(0, 6, 6, 5, 31, 82, 1)
    s.box(44, 6, 6, 4, 31, 82, 1)

    for z in (57, 72):
        s.box(48, 6, z, 30, 31, 3, 1)
    s.box(48, 6, 6, 30, 31, 42, 1)
    for z in (20, 34):
        s.line([(48, 37.1, z), (77, 37.1, z)], EDGE)
    for z in (14, 28, 42):
        s.line([(58, 37.1, z), (68, 37.1, z)], EDGE)

    s.tube([(4, 23, 72), (44, 23, 72)], 1.15)
    for x in (15, 31):
        s.line([(x, 25, 72), (x + 1, 25, 66), (x - 6, 25, 59),
                (x + 8, 25, 59), (x + 1, 25, 66)], EDGE)
    s.box(77, 0, 6, 5, 37, 82, 1)
    s.box(0, 0, 88, 82, 37, 6, 1)
    s.line([(5, 37, 7), (5, 37, 87)], DETAIL)
