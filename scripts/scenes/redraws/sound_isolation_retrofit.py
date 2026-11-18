from geometry import DETAIL, EDGE, oval

DESCRIPTION = "Two sound waves approach a wall cutaway with an acoustic batt fitted between its studs and doubled lining."


def draw(s):
    s.box(-35, -7, 0, 70, 14, 53, .5)
    s.box(-35, 7, 0, 5, 12, 53, .5)
    s.box(-3, 7, 0, 5, 12, 53, .5)
    s.box(-30, 7, 0, 27, 12, 4, .5)
    s.box(-30, 7, 49, 27, 12, 4, .5)
    s.face([(-30, 16, 4), (-3, 16, 4), (-3, 16, 49), (-30, 16, 49)], EDGE)

    # The alternating folds stay inside the exposed cavity.
    wool = []
    for z, end in ((12, 450), (20, 90), (28, 450), (36, 90), (44, 450)):
        wool.extend(oval(-17, z, 9, 4, 270, end, 18))
    s.line([(x, 16, z) for x, z in wool], DETAIL)
    s.box(2, 7, 0, 33, 12, 53, .5)
    s.box(1, 19, 0, 34, 2, 53, .5)
    s.box(0, 21, 0, 35, 2, 53, .5)
    s.line([(0, 23, 6), (35, 23, 6)], DETAIL)

    for radius in (14, 22):
        s.line([(67 + .577 * u, -10 - .577 * u, 28 + 1.15 * v)
                for u, v in oval(0, 0, radius, radius, 143, 217, 22)], EDGE)
