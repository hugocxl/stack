from geometry import DETAIL, EDGE, oval

DESCRIPTION = "Two rooms in a cutaway floor plan each contain a wall manifold and an independent radiant heating loop."


def draw(s):
    s.box(-45, -29, 0, 90, 59, 4, 1)
    s.box(-45, -29, 4, 90, 3, 12, .5)
    s.box(-45, -26, 4, 3, 56, 9, .5)
    for x in (-22, 22):
        s.box(x - 10, -25, 5, 20, 4, 7, .9)
        s.line([(x - 6, -21, 8.5), (x + 6, -21, 8.5)], DETAIL)
        for valve in (-6, 6):
            s.line([(x + valve, -21, 12), (x + valve, -21, 5)], EDGE)
        loop = [(x - 6, -21), (x - 6, -18), (x - 15, -12)]
        loop += oval(x - 10, 17, 5, 5, 180, 0, 18)
        loop += oval(x, -10, 5, 5, 180, 360, 18)
        loop += oval(x + 10, 17, 5, 5, 180, 0, 18)
        loop += [(x + 15, -12), (x + 6, -18), (x + 6, -21)]
        s.line([(u, v, 4.5) for u, v in loop], EDGE)

    s.box(-1.5, -26, 4, 3, 53, 8, .5)
    s.box(42, -26, 4, 3, 56, 7, .5)
    for left, width in ((-42, 13), (-13, 26), (29, 13)):
        s.box(left, 27, 4, width, 3, 5, .5)
