from geometry import DETAIL, EDGE

DESCRIPTION = "A storefront cutaway shows a fitted merchandise display and a built-in service counter under its shopfront canopy."


def draw(s):
    s.box(0, 0, 0, 90, 58, 5, 2)
    s.box(0, 0, 5, 90, 5, 56, 1)
    s.box(0, 5, 5, 5, 53, 53, 1)
    s.box(5, 38, 5, 34, 14, 21, 1)
    s.box(4, 37, 26, 36, 16, 3, 1)

    # The two shelf ledges belong to the single fitted display.
    s.box(47, 5, 6, 36, 3, 43, 1)
    for z in (9, 25, 42):
        s.box(47, 8, z, 36, 10, 2, 1)
    for x, z, w, h in ((50, 11, 9, 9), (65, 11, 12, 7),
                       (51, 27, 12, 9), (68, 27, 9, 11)):
        s.box(x, 8, z, w, 8, h, 1, DETAIL)

    # Open roof and a short front fascia preserve the view into the shop.
    s.box(0, 0, 58, 90, 7, 8, 1)
    s.box(0, 53, 54, 90, 7, 9, 1)
    s.box(0, 6, 58, 6, 48, 5, 1)
    s.box(84, 54, 5, 5, 5, 49, 1)
    s.box(0, 53, 5, 5, 6, 49, 1)
    s.face([(1, 56, 63), (60, 56, 63), (60, 67, 54), (1, 67, 54)], EDGE)
    s.face([(1, 67, 54), (60, 67, 54), (60, 67, 51), (1, 67, 51)], EDGE)
    for x in (13, 25, 37, 49):
        s.line([(x, 56, 63), (x, 67, 54), (x, 67, 51)], DETAIL)
